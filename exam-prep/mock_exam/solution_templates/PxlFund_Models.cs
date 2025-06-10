using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;

namespace PxlFund.Mvc.Models
{
    // === BANK ENTITY ===
    public class Bank
    {
        public int Id { get; set; }

        [Required(ErrorMessage = "Bank name is required")]
        [StringLength(50, ErrorMessage = "Bank name cannot exceed 50 characters")]
        [Display(Name = "Bank Name")]
        public string Name { get; set; } = string.Empty;

        [StringLength(200, ErrorMessage = "Description cannot exceed 200 characters")]
        [Display(Name = "Description")]
        public string? Description { get; set; }

        [Display(Name = "Is Active")]
        public bool IsActive { get; set; } = true;

        [Display(Name = "Created Date")]
        [DataType(DataType.DateTime)]
        public DateTime CreatedDate { get; set; } = DateTime.Now;

        // Navigation property - One Bank has many Funds
        public virtual ICollection<Fund>? Funds { get; set; }
    }

    // === FUND ENTITY ===
    public class Fund
    {
        public int Id { get; set; }

        [Required(ErrorMessage = "Fund name is required")]
        [StringLength(100, MinimumLength = 2, ErrorMessage = "Fund name must be between 2 and 100 characters")]
        [Display(Name = "Fund Name")]
        public string Name { get; set; } = string.Empty;

        [StringLength(500, ErrorMessage = "Description cannot exceed 500 characters")]
        [Display(Name = "Fund Description")]
        [DataType(DataType.MultilineText)]
        public string? Description { get; set; }

        [Required(ErrorMessage = "Fund value is required")]
        [DataType(DataType.Currency)]
        [Range(0.01, 999999.99, ErrorMessage = "Fund value must be between €0.01 and €999,999.99")]
        [Display(Name = "Fund Value (EUR)")]
        [Precision(10, 2)]
        public decimal Value { get; set; }

        [Required(ErrorMessage = "Bank is required")]
        [Display(Name = "Bank")]
        public int BankId { get; set; }

        [StringLength(20, ErrorMessage = "Fund type cannot exceed 20 characters")]
        [Display(Name = "Fund Type")]
        public string? FundType { get; set; } // e.g., "Green", "Yellow", "Brown", "Black"

        [Display(Name = "Is Active")]
        public bool IsActive { get; set; } = true;

        [Display(Name = "Minimum Investment")]
        [DataType(DataType.Currency)]
        [Range(0, double.MaxValue, ErrorMessage = "Minimum investment must be positive")]
        [Precision(10, 2)]
        public decimal? MinimumInvestment { get; set; }

        [Display(Name = "Created Date")]
        [DataType(DataType.DateTime)]
        public DateTime CreatedDate { get; set; } = DateTime.Now;

        // Navigation properties
        [ForeignKey("BankId")]
        public virtual Bank? Bank { get; set; }

        public virtual ICollection<UserFund>? UserFunds { get; set; }
    }

    // === USER FUND BRIDGE ENTITY (Many-to-Many) ===
    public class UserFund
    {
        public int Id { get; set; }

        [Required(ErrorMessage = "User is required")]
        public string UserId { get; set; } = string.Empty;

        [Required(ErrorMessage = "Fund is required")]
        public int FundId { get; set; }

        [Required(ErrorMessage = "Investment amount is required")]
        [DataType(DataType.Currency)]
        [Range(0.01, double.MaxValue, ErrorMessage = "Investment amount must be greater than 0")]
        [Display(Name = "Investment Amount (EUR)")]
        [Precision(10, 2)]
        public decimal InvestmentAmount { get; set; }

        [Display(Name = "Investment Date")]
        [DataType(DataType.DateTime)]
        public DateTime InvestmentDate { get; set; } = DateTime.Now;

        [StringLength(500, ErrorMessage = "Notes cannot exceed 500 characters")]
        [Display(Name = "Investment Notes")]
        public string? Notes { get; set; }

        [Display(Name = "Is Active")]
        public bool IsActive { get; set; } = true;

        // Calculated property for current value (could be enhanced with market data)
        [NotMapped]
        [Display(Name = "Current Value")]
        public decimal CurrentValue => InvestmentAmount; // Simplified - in real system would calculate based on market performance

        // Navigation properties
        [ForeignKey("UserId")]
        public virtual PxlFundUser? User { get; set; }

        [ForeignKey("FundId")]
        public virtual Fund? Fund { get; set; }
    }

    // === CUSTOM USER ENTITY (Extends Identity) ===
    public class PxlFundUser : IdentityUser
    {
        [StringLength(50, ErrorMessage = "First name cannot exceed 50 characters")]
        [Display(Name = "First Name")]
        public string? FirstName { get; set; }

        [StringLength(50, ErrorMessage = "Last name cannot exceed 50 characters")]
        [Display(Name = "Last Name")]
        public string? LastName { get; set; }

        [NotMapped]
        [Display(Name = "Full Name")]
        public string FullName => string.IsNullOrEmpty(FirstName) || string.IsNullOrEmpty(LastName) 
            ? UserName ?? Email ?? "Unknown User" 
            : $"{FirstName} {LastName}";

        [DataType(DataType.Date)]
        [Display(Name = "Date of Birth")]
        public DateTime? DateOfBirth { get; set; }

        [StringLength(200, ErrorMessage = "Address cannot exceed 200 characters")]
        [Display(Name = "Address")]
        public string? Address { get; set; }

        [StringLength(50, ErrorMessage = "City cannot exceed 50 characters")]
        [Display(Name = "City")]
        public string? City { get; set; }

        [StringLength(20, ErrorMessage = "Postal code cannot exceed 20 characters")]
        [Display(Name = "Postal Code")]
        public string? PostalCode { get; set; }

        [Display(Name = "Registration Date")]
        [DataType(DataType.DateTime)]
        public DateTime RegistrationDate { get; set; } = DateTime.Now;

        [Display(Name = "Is Active")]
        public bool IsActive { get; set; } = true;

        [Display(Name = "Investment Portfolio Value")]
        [DataType(DataType.Currency)]
        [NotMapped]
        public decimal TotalInvestmentValue => UserFunds?.Where(uf => uf.IsActive).Sum(uf => uf.CurrentValue) ?? 0;

        [Display(Name = "Number of Investments")]
        [NotMapped]
        public int ActiveInvestmentCount => UserFunds?.Count(uf => uf.IsActive) ?? 0;

        // Navigation properties
        public virtual ICollection<UserFund>? UserFunds { get; set; }
    }

    // === VIEW MODELS FOR API RESPONSES ===
    public class FundInfoResponse
    {
        public string BankName { get; set; } = string.Empty;
        public string FundName { get; set; } = string.Empty;
        public decimal FundValue { get; set; }
        public string FundType { get; set; } = string.Empty;
        public bool IsActive { get; set; }
    }

    public class AddFundRequest
    {
        [Required(ErrorMessage = "Fund name is required")]
        [StringLength(100, ErrorMessage = "Fund name cannot exceed 100 characters")]
        public string Name { get; set; } = string.Empty;

        [StringLength(500, ErrorMessage = "Description cannot exceed 500 characters")]
        public string? Description { get; set; }

        [Required(ErrorMessage = "Fund value is required")]
        [Range(0.01, 999999.99, ErrorMessage = "Fund value must be between €0.01 and €999,999.99")]
        public decimal Value { get; set; }

        [StringLength(20, ErrorMessage = "Fund type cannot exceed 20 characters")]
        public string? FundType { get; set; }

        [Range(0, double.MaxValue, ErrorMessage = "Minimum investment must be positive")]
        public decimal? MinimumInvestment { get; set; }
    }

    // === BLAZOR COMPONENT VIEW MODELS ===
    public class AddUserFundViewModel
    {
        [Required(ErrorMessage = "Please select a fund")]
        [Display(Name = "Fund")]
        public int FundId { get; set; }

        [Required(ErrorMessage = "Investment amount is required")]
        [Range(0.01, double.MaxValue, ErrorMessage = "Investment amount must be greater than 0")]
        [Display(Name = "Investment Amount (EUR)")]
        public decimal InvestmentAmount { get; set; }

        [StringLength(500, ErrorMessage = "Notes cannot exceed 500 characters")]
        [Display(Name = "Notes")]
        public string? Notes { get; set; }

        // For dropdown population
        public List<Fund>? AvailableFunds { get; set; }
    }

    public class UserFundOverviewViewModel
    {
        public string UserId { get; set; } = string.Empty;
        public string UserName { get; set; } = string.Empty;
        public List<UserFundDetailViewModel> UserFunds { get; set; } = new();
        public decimal TotalInvestmentValue { get; set; }
        public int TotalFundCount { get; set; }
    }

    public class UserFundDetailViewModel
    {
        public int UserFundId { get; set; }
        public string FundName { get; set; } = string.Empty;
        public string BankName { get; set; } = string.Empty;
        public string FundType { get; set; } = string.Empty;
        public decimal InvestmentAmount { get; set; }
        public decimal FundValue { get; set; }
        public DateTime InvestmentDate { get; set; }
        public string? Notes { get; set; }
        public bool IsActive { get; set; }
    }
}

/* 
=== EXAM-SPECIFIC IMPLEMENTATION NOTES ===

SEEDING DATA (for SeedDataRepository):
Banks:
- KBC
- Argenta

Funds:
- KBC Green (KBC, 100 EUR)
- KBC Yellow (KBC, 125 EUR)  
- ARG Brown (Argenta, 135 EUR)
- ARG Black (Argenta, 140 EUR)

Users & Roles:
- Admin role
- Client role
- Admin user: admin@pxl.be / Adm!n

=== RELATIONSHIPS SUMMARY ===
Bank (1) → (Many) Fund
User (1) → (Many) UserFund ← (Many) Fund
= User ↔ Fund Many-to-Many through UserFund

=== API RESPONSE FORMATS ===
GET /api/FundInfo:
{
  "bankName": "KBC",
  "fundName": "KBC Green", 
  "fundValue": 100.00
}

POST /api/Fund/KBC:
{
  "name": "New Fund Name",
  "value": 150.00,
  "fundType": "Blue"
}

=== BLAZOR COMPONENTS NEEDED ===
1. AddUserFund.razor - Form to add fund to user portfolio
2. UserFundsOverview.razor - Display user's current funds

=== VALIDATION HIGHLIGHTS ===
- All required fields have proper error messages
- Currency values use Precision(10, 2)
- String lengths match expected banking data
- Date fields use proper DataType attributes
- Navigation properties support lazy loading

=== USAGE IN EXAM ===
1. Copy this file to Models/
2. Update namespace if different
3. Ensure all using statements are included
4. Add to DbContext as DbSet<Bank>, DbSet<Fund>, DbSet<UserFund>
5. Configure relationships in OnModelCreating if needed
6. Run Add-Migration and Update-Database
*/