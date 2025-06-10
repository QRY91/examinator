using Microsoft.AspNetCore.Identity;
using System.ComponentModel.DataAnnotations;

namespace BookHaven.Models
{
    public class ApplicationUser : IdentityUser
    {
        [Required]
        [Display(Name = "First Name")]
        public string FirstName { get; set; } = string.Empty;
        
        [Required]
        [Display(Name = "Last Name")]
        public string LastName { get; set; } = string.Empty;
        
        [Display(Name = "Full Name")]
        public string FullName => $"{FirstName} {LastName}";
        
        public DateTime RegistrationDate { get; set; } = DateTime.Now;
    }
} 