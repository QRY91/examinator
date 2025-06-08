# C# MVC Web Shop Comprehensive Summary

## 📚 ASP.NET Core MVC Architecture & Patterns

### 1. What is the MVC (Model-View-Controller) pattern?

<details>
<summary>🤔 Click to reveal answer</summary>

An architectural pattern that separates application logic into three interconnected components:
- **Model**: Data and business logic (entities, validation, database interactions)
- **View**: User interface presentation layer (Razor pages, HTML)
- **Controller**: Handles user input and coordinates between Model and View

This separation provides better organization, testability, and maintainability.

</details>

### 2. What is the role of Controllers in ASP.NET Core MVC?

<details>
<summary>🤔 Click to reveal answer</summary>

Controllers handle HTTP requests, process user input, interact with models, and return appropriate responses (Views, JSON, redirects). They act as the entry point for web requests and coordinate application flow.

Example: `ProductController` handles product-related operations like listing, filtering, and CRUD operations.

</details>

### 3. What is Dependency Injection in ASP.NET Core?

<details>
<summary>🤔 Click to reveal answer</summary>

A design pattern where dependencies are provided to a class rather than created internally. ASP.NET Core has built-in DI container that manages object lifetimes and resolves dependencies.

Example: `ProductController` receives `IProductRepository` through constructor injection, promoting loose coupling and testability.

</details>

### 4. What are Action Methods in Controllers?

<details>
<summary>🤔 Click to reveal answer</summary>

Public methods in controllers that handle HTTP requests and return `IActionResult`. They can accept parameters from routes, query strings, or request bodies.

Example: `Index(string searchString, List<string> selectedCategories, decimal? minPrice, decimal? maxPrice, int page = 1)`

</details>

## 📊 Data Models and Entity Relationships

### 5. What is the Product model structure in this webshop?

<details>
<summary>🤔 Click to reveal answer</summary>

The Product model contains:
- **Identity**: `Id` (primary key)
- **Basic Info**: `Name`, `Price`, `Color`, `Year`, `SerialNumber`
- **Relationships**: `CategoryId` (foreign key), `Category` (navigation property)
- **Features**: `ImageUrl`, `IsFeatured` (boolean flag)
- **Validation**: Required fields, data types, regular expressions

</details>

### 6. How does the Order-Orderline relationship work?

<details>
<summary>🤔 Click to reveal answer</summary>

**One-to-Many relationship**:
- Order can have multiple Orderlines: `List<Orderline> Orderlines`
- Each Orderline belongs to one Order
- Orderlines contain specific products and quantities for an order
- This follows the shopping cart pattern where one order contains multiple items

</details>

### 7. What is the Customer-BrixelUser relationship?

<details>
<summary>🤔 Click to reveal answer</summary>

**One-to-One relationship**:
- Customer has `BrixelUserId` foreign key pointing to `BrixelUser`
- `BrixelUser` extends ASP.NET Core Identity's `IdentityUser`
- Separates authentication (BrixelUser) from business data (Customer)
- Allows users without customer profiles (admins, employees)

</details>

### 8. How does guest cart functionality work in Orders?

<details>
<summary>🤔 Click to reveal answer</summary>

Orders support both authenticated and guest users:
- **Authenticated**: `CustomerId` points to registered customer
- **Guest**: `GuestCartId` stores GUID from browser cookie
- **Detection**: `IsGuestCart` property checks if both `CustomerId` and `GuestCartId` exist
- Enables shopping without registration while maintaining cart persistence

</details>

## ✅ Validation and Data Annotations

### 9. What validation attributes are used in the Product model?

<details>
<summary>🤔 Click to reveal answer</summary>

- **[Required]**: Ensures Name, Price, Color, ImageUrl are provided
- **[DataType(DataType.Currency)]**: Specifies Price as currency
- **[Precision(10, 2)]**: Defines decimal precision for Price
- **[RegularExpression]**: Validates Color as hex format (#RRGGBB or #RGB)
- **[DataType(DataType.Url)]**: Validates ImageUrl format
- **[Range(1900, 9999)]**: Validates Year within reasonable range

</details>

### 10. What is the purpose of ErrorMessage in validation attributes?

<details>
<summary>🤔 Click to reveal answer</summary>

Provides custom user-friendly error messages when validation fails, instead of default generic messages.

Example: `[Required(ErrorMessage = "Name is required")]` shows "Name is required" instead of "The Name field is required."

</details>

### 11. How does the [EmailAddress] attribute work?

<details>
<summary>🤔 Click to reveal answer</summary>

Validates that the property value matches standard email format patterns. Used on `Customer.DeliveryMail` to ensure valid email addresses for order notifications.

Built-in validation that checks for @ symbol, domain structure, and basic email formatting rules.

</details>

### 12. What are nullable reference types in C#?

<details>
<summary>🤔 Click to reveal answer</summary>

Types that can hold `null` values, indicated by `?` suffix:
- **Value types**: `int?`, `decimal?` - can be null or have value
- **Reference types**: `string?`, `Category?` - explicitly nullable in C# 8+
- **Purpose**: Express intent about whether null is expected, helping prevent null reference exceptions

</details>

## 🗄️ Entity Framework and Database Concepts

### 13. What is Entity Framework Core?

<details>
<summary>🤔 Click to reveal answer</summary>

An Object-Relational Mapping (ORM) framework that enables .NET developers to work with databases using .NET objects. It handles database connections, query translation, and change tracking automatically.

</details>

### 14. What are Navigation Properties?

<details>
<summary>🤔 Click to reveal answer</summary>

Properties that represent relationships between entities:
- **Product.Category**: Reference navigation (many-to-one)
- **Order.Orderlines**: Collection navigation (one-to-many)
- Enable lazy loading and eager loading of related data
- EF Core uses these to understand database relationships

</details>

### 15. What is the [ForeignKey] attribute?

<details>
<summary>🤔 Click to reveal answer</summary>

Explicitly specifies which property serves as the foreign key for a navigation property.

Example: `[ForeignKey(nameof(BrixelUser))] public string BrixelUserId` tells EF Core that `BrixelUserId` is the foreign key for the `BrixelUser` navigation property.

</details>

### 16. What is the Repository Pattern?

<details>
<summary>🤔 Click to reveal answer</summary>

A design pattern that encapsulates data access logic and provides a uniform interface for accessing data. 

Example: `IProductRepository` abstracts database operations, making the controller independent of specific data access implementation and improving testability.

</details>

## 🎮 Controller Patterns and Logic

### 17. How does search functionality work in ProductController?

<details>
<summary>🤔 Click to reveal answer</summary>

Multi-field search using LINQ:
1. **Text search**: Checks product name and category name using `Contains()` with `StringComparison.OrdinalIgnoreCase`
2. **Category filtering**: Filters by selected category names
3. **Price range**: Applies min/max price filters
4. **Chaining**: Filters are applied sequentially using LINQ `Where()` methods

</details>

### 18. How is pagination implemented?

<details>
<summary>🤔 Click to reveal answer</summary>

Standard pagination pattern:
1. **Count total**: Get total items before pagination for page calculation
2. **Skip/Take**: Use `Skip((page - 1) * pageSize).Take(pageSize)`
3. **ViewBag data**: Pass current page, total pages, and page size to view
4. **Page calculation**: `Math.Ceiling((double)totalItems / pageSize)`

</details>

### 19. What HTTP verbs and routing are used?

<details>
<summary>🤔 Click to reveal answer</summary>

RESTful conventions:
- **GET /Product**: List products (Index action)
- **GET /Product/Details/5**: Show specific product
- **GET /Product/Create**: Show create form
- **POST /Product/Create**: Process new product
- **GET /Product/Edit/5**: Show edit form
- **POST /Product/Edit/5**: Process updates

</details>

### 20. What is [ValidateAntiForgeryToken]?

<details>
<summary>🤔 Click to reveal answer</summary>

Security attribute that prevents Cross-Site Request Forgery (CSRF) attacks by validating that POST requests include a valid anti-forgery token generated by the server.

Essential for any action that modifies data (Create, Edit, Delete operations).

</details>

## 🔐 Identity and Authentication

### 21. How does ASP.NET Core Identity work in this application?

<details>
<summary>🤔 Click to reveal answer</summary>

Uses `IdentityUser` as base class for `BrixelUser`:
- **Authentication**: Login/logout functionality
- **Authorization**: Role-based access control
- **User Management**: Registration, password management
- **Extension**: `BrixelUser` adds custom properties while maintaining Identity features

</details>

### 22. What is the purpose of the BrixelUser class?

<details>
<summary>🤔 Click to reveal answer</summary>

Extends `IdentityUser` to add application-specific properties:
- **CustomerId**: Links to Customer profile (nullable for non-customers)
- **Constructors**: Supports both parameterless and username-based initialization
- **Flexibility**: Allows users without customer profiles (admins, employees)

</details>

### 23. How are user roles typically handled?

<details>
<summary>🤔 Click to reveal answer</summary>

Through ASP.NET Core Identity's role system:
- **Customer role**: Users with customer profiles for shopping
- **Admin role**: Users who manage products, orders, and system
- **Employee role**: Users with limited administrative access
- Roles control access to different controllers and actions

</details>

## 💰 Business Logic and Calculations

### 24. How are order totals calculated?

<details>
<summary>🤔 Click to reveal answer</summary>

Multi-step calculation in Order model:
- **GrossTotal**: Sum of all orderline subtotals (quantity × price)
- **VatTotal**: Tax amount applied to gross total
- **AppliedDiscount**: Discount amount (could be percentage or fixed)
- **GrandTotal**: Computed property: `GrossTotal + VatTotal - AppliedDiscount`

</details>

### 25. What are computed properties in C#?

<details>
<summary>🤔 Click to reveal answer</summary>

Properties that calculate their value from other properties rather than storing data:

Example: `public decimal GrandTotal => GrossTotal + VatTotal - (decimal)AppliedDiscount;`

These provide real-time calculations and ensure consistency without storing redundant data.

</details>

### 26. How does order status tracking work?

<details>
<summary>🤔 Click to reveal answer</summary>

Through Status entity relationship:
- **StatusId**: Foreign key to Status table
- **Status**: Navigation property for eager loading
- **OrderDate**: Timestamp for order creation
- Enables order lifecycle tracking (Pending → Processing → Shipped → Delivered)

</details>

## 🎨 View and Data Transfer

### 27. What is ViewBag and how is it used?

<details>
<summary>🤔 Click to reveal answer</summary>

Dynamic object for passing data from controller to view:
- **Search data**: `ViewBag.SearchString`, `ViewBag.SelectedCategories`
- **Pagination**: `ViewBag.CurrentPage`, `ViewBag.TotalPages`
- **Form data**: `ViewBag.Categories` for dropdown lists
- **Filters**: `ViewBag.MinPrice`, `ViewBag.MaxPrice`

ViewBag is dynamic but lacks compile-time checking; ViewModels are preferred for complex scenarios.

</details>

### 28. What is the difference between ViewBag, ViewData, and TempData?

<details>
<summary>🤔 Click to reveal answer</summary>

- **ViewBag**: Dynamic object, data available only in current request
- **ViewData**: Dictionary-based, data available only in current request  
- **TempData**: Dictionary-based, data survives redirect and is removed after next request
- **Scope**: ViewBag/ViewData for controller-to-view, TempData for controller-to-controller

</details>

## 🔧 Advanced Patterns and Concepts

### 29. What is StringComparison.OrdinalIgnoreCase?

<details>
<summary>🤔 Click to reveal answer</summary>

A string comparison method that:
- **Case-insensitive**: "Product" matches "product" and "PRODUCT"
- **Ordinal**: Uses raw character values without cultural rules
- **Performance**: Faster than culture-aware comparisons
- **Use case**: Ideal for search functionality where case shouldn't matter

</details>

### 30. How does LINQ method chaining work in the search?

<details>
<summary>🤔 Click to reveal answer</summary>

Fluent interface pattern where each LINQ method returns `IQueryable`:
```csharp
filteredProducts = allProducts.AsQueryable()
    .Where(p => p.Name.Contains(searchString))
    .Where(p => selectedCategories.Contains(p.Category.Name))
    .Where(p => p.Price >= minPrice)
    .Skip((page - 1) * pageSize)
    .Take(pageSize);
```
Each `Where()` further filters the result set without executing until enumerated.

</details>

### 31. What is the async/await pattern in controllers?

<details>
<summary>🤔 Click to reveal answer</summary>

Asynchronous programming pattern for non-blocking operations:
- **async Task<IActionResult>**: Marks method as asynchronous
- **await**: Waits for async operation without blocking thread
- **Repository calls**: `await _productRepository.GetAll()` for database operations
- **Benefits**: Better scalability and responsiveness for I/O operations

</details>

### 32. How does model binding work in action parameters?

<details>
<summary>🤔 Click to reveal answer</summary>

ASP.NET Core automatically maps HTTP request data to action parameters:
- **Query strings**: `?searchString=laptop&page=2` maps to method parameters
- **Route values**: `/Product/Details/5` maps `id` parameter
- **Form data**: POST form fields map to model properties
- **JSON**: Request body JSON maps to complex objects
- **Collections**: Multiple values map to `List<string>` parameters

</details>

---

📖 **[Return to Wiki Home](Home)**

🎯 **[Back to Examinator](https://github.com/QRY91/examinator)**