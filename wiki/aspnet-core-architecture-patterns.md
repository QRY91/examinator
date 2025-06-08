# ASP.NET Core Architecture & Patterns Summary

## 🏗️ ASP.NET Core Fundamentals

### 1. What is ASP.NET Core and how does it differ from .NET Framework?

<details>
<summary>🤔 Click to reveal answer</summary>

ASP.NET Core is a cross-platform, high-performance framework for building modern web applications:
- **Cross-platform**: Runs on Windows, macOS, and Linux
- **Open source**: Fully open source with community contributions
- **Performance**: Significantly faster than .NET Framework
- **Modular**: Pay-for-play model - only include what you need
- **Cloud-ready**: Built for containerization and cloud deployment
- **Unified**: Web APIs and MVC in single framework

</details>

### 2. What is the Program.cs file and how has it evolved?

<details>
<summary>🤔 Click to reveal answer</summary>

The application entry point that configures services and middleware:
- **Minimal hosting model**: Single file configuration (NET 6+)
- **Service registration**: `builder.Services.AddControllers()`
- **Middleware pipeline**: `app.UseRouting()`, `app.UseAuthentication()`
- **Environment-specific**: Different configurations for Development/Production
- **Dependency injection**: Built-in container configuration

</details>

### 3. What is the difference between services and middleware?

<details>
<summary>🤔 Click to reveal answer</summary>

**Services**:
- Registered in DI container during startup
- Provide functionality throughout application lifetime
- Examples: Repository classes, database contexts, authentication services

**Middleware**:
- Components in the request pipeline
- Process HTTP requests and responses
- Examples: Authentication, routing, error handling, static files
- Order matters - pipeline executes in sequence

</details>

## 🔧 Dependency Injection Deep Dive

### 4. What are the three service lifetimes in ASP.NET Core?

<details>
<summary>🤔 Click to reveal answer</summary>

- **Singleton**: Single instance for entire application lifetime
  - `services.AddSingleton<IService, Service>()`
  - Use for stateless services, expensive-to-create objects
  
- **Scoped**: One instance per HTTP request
  - `services.AddScoped<IService, Service>()`
  - Use for database contexts, request-specific services
  
- **Transient**: New instance every time requested
  - `services.AddTransient<IService, Service>()`
  - Use for lightweight, stateless services

</details>

### 5. How does constructor injection work in controllers?

<details>
<summary>🤔 Click to reveal answer</summary>

Controllers receive dependencies through constructor parameters:
```csharp
public class ProductController : Controller
{
    private readonly IProductRepository _repository;
    private readonly ILogger<ProductController> _logger;
    
    public ProductController(IProductRepository repository, ILogger<ProductController> logger)
    {
        _repository = repository;
        _logger = logger;
    }
}
```
ASP.NET Core's DI container automatically resolves and injects registered services.

</details>

### 6. What are the benefits of using interfaces with DI?

<details>
<summary>🤔 Click to reveal answer</summary>

- **Loose coupling**: Controller depends on abstraction, not concrete implementation
- **Testability**: Easy to mock interfaces for unit testing
- **Flexibility**: Swap implementations without changing dependent code
- **SOLID principles**: Follows Dependency Inversion Principle
- **Configuration**: Different implementations for different environments

</details>

## 🚀 Middleware Pipeline

### 7. How does the middleware pipeline work?

<details>
<summary>🤔 Click to reveal answer</summary>

Request flows through middleware components in order:
1. **Request path**: Each middleware can process request
2. **Chain**: Calls `next()` to pass to next middleware
3. **Response path**: Processes response in reverse order
4. **Short-circuiting**: Middleware can end pipeline early

Common order: Exception → HTTPS → Static Files → Routing → Authentication → Authorization → Endpoints

</details>

### 8. What is the purpose of UseRouting() middleware?

<details>
<summary>🤔 Click to reveal answer</summary>

Determines which endpoint should handle the request:
- **Route matching**: Matches URL patterns to actions
- **Parameter extraction**: Extracts route values (id, action, controller)
- **Endpoint selection**: Selects the appropriate controller action
- **Must come before**: Authentication/Authorization middleware that need route info

</details>

### 9. What does UseAuthentication() vs UseAuthorization() do?

<details>
<summary>🤔 Click to reveal answer</summary>

**UseAuthentication()**:
- Identifies WHO the user is
- Validates authentication tokens/cookies
- Sets `HttpContext.User` identity
- Must come before authorization

**UseAuthorization()**:
- Determines WHAT the user can do
- Checks roles, policies, and permissions
- Blocks unauthorized access to protected resources
- Depends on user identity from authentication

</details>

## 🗺️ Routing and URL Patterns

### 10. How does conventional routing work in MVC?

<details>
<summary>🤔 Click to reveal answer</summary>

Default pattern: `{controller=Home}/{action=Index}/{id?}`
- **Controller**: Maps to controller class name (without "Controller")
- **Action**: Maps to public method in controller
- **Optional parameters**: `?` makes parameter optional
- **Defaults**: Specified with `=` operator
- **Constraints**: Can add type/format constraints

Example: `/Product/Details/5` → `ProductController.Details(id: 5)`

</details>

### 11. What is attribute routing and when should you use it?

<details>
<summary>🤔 Click to reveal answer</summary>

Route attributes directly on controllers/actions:
```csharp
[Route("api/products")]
public class ProductController : Controller
{
    [HttpGet("{id:int}")]
    public IActionResult GetProduct(int id) { }
}
```

**Use when**:
- RESTful APIs with specific URL patterns
- Complex routing requirements
- Need precise control over URLs
- Building Web APIs

</details>

### 12. What are route constraints and how do they work?

<details>
<summary>🤔 Click to reveal answer</summary>

Restrict which requests match a route:
- **Type constraints**: `{id:int}`, `{price:decimal}`
- **Format constraints**: `{date:datetime}`, `{guid:guid}`
- **Range constraints**: `{page:int:min(1)}`
- **Regex constraints**: `{code:regex(^[A-Z]{{3}}$)}`

Ensures parameters meet requirements before action is called.

</details>

## 📝 Model Binding and Validation

### 13. How does model binding work in ASP.NET Core?

<details>
<summary>🤔 Click to reveal answer</summary>

Automatically maps HTTP request data to action parameters:
1. **Route values**: `/Product/Details/5` → `id = 5`
2. **Query string**: `?name=laptop&page=2`
3. **Form data**: POST form fields
4. **Request body**: JSON/XML for APIs
5. **Headers**: Custom headers if specified

Order: Route → Query String → Form → Body

</details>

### 14. What are binding sources and when do you use them?

<details>
<summary>🤔 Click to reveal answer</summary>

Attributes that specify where to get parameter values:
- **[FromRoute]**: From URL route values
- **[FromQuery]**: From query string parameters
- **[FromForm]**: From form data
- **[FromBody]**: From request body (JSON/XML)
- **[FromHeader]**: From HTTP headers
- **[FromServices]**: From dependency injection container

Useful when automatic binding is ambiguous or insufficient.

</details>

### 15. How does server-side validation work?

<details>
<summary>🤔 Click to reveal answer</summary>

Multi-layer validation approach:
1. **Data Annotations**: `[Required]`, `[Range]`, `[EmailAddress]`
2. **Model State**: `ModelState.IsValid` checks all validations
3. **Custom Validation**: `IValidatableObject`, custom attributes
4. **Client-side**: JavaScript validation for better UX
5. **Error Display**: Validation helpers in Razor views

Always validate server-side even with client validation.

</details>

## 🔐 Authentication and Authorization

### 16. What authentication schemes are available in ASP.NET Core?

<details>
<summary>🤔 Click to reveal answer</summary>

- **Cookie Authentication**: Traditional web apps with login forms
- **JWT Bearer**: APIs and SPAs with JSON Web Tokens
- **Identity**: Full-featured user management system
- **External Providers**: Google, Facebook, Microsoft OAuth
- **Windows Authentication**: Domain-based authentication
- **Certificate Authentication**: Client certificate validation

</details>

### 17. How do authorization policies work?

<details>
<summary>🤔 Click to reveal answer</summary>

Fine-grained permission system:
```csharp
services.AddAuthorization(options =>
{
    options.AddPolicy("AdminOnly", policy => 
        policy.RequireRole("Admin"));
    options.AddPolicy("MinAge18", policy => 
        policy.RequireClaim("Age", "18", "19", "20"...));
});
```

Apply with `[Authorize(Policy = "AdminOnly")]` on controllers/actions.

</details>

### 18. What is the difference between authentication and authorization?

<details>
<summary>🤔 Click to reveal answer</summary>

**Authentication** (Who are you?):
- Verifies user identity
- Login process with credentials
- Issues authentication token/cookie
- `HttpContext.User.Identity.IsAuthenticated`

**Authorization** (What can you do?):
- Determines permissions and access rights
- Checks roles, policies, claims
- Protects resources and actions
- `[Authorize]` attributes and policies

</details>

## ⚡ Performance and Optimization

### 19. What is output caching and when should you use it?

<details>
<summary>🤔 Click to reveal answer</summary>

Stores rendered page output to serve repeated requests faster:
- **Page-level**: Cache entire page responses
- **Partial-level**: Cache parts of pages (ViewComponents)
- **Distributed**: Share cache across multiple servers
- **Vary by**: Cache different versions by user, parameters, headers

Use for: Static content, expensive database queries, rarely-changing data.

</details>

### 20. How does response compression work?

<details>
<summary>🤔 Click to reveal answer</summary>

Reduces response size using compression algorithms:
- **Gzip**: Most common compression format
- **Brotli**: Better compression, newer browsers
- **Automatic**: Negotiates best compression with client
- **Selective**: Compress only certain content types
- **Configuration**: Set compression levels and thresholds

Significantly reduces bandwidth usage and improves performance.

</details>

### 21. What are the benefits of async/await in web applications?

<details>
<summary>🤔 Click to reveal answer</summary>

**Scalability**: Threads aren't blocked waiting for I/O operations
- **Thread pool efficiency**: More requests handled with same threads
- **Database calls**: `await dbContext.SaveChangesAsync()`
- **HTTP calls**: `await httpClient.GetAsync()`
- **File operations**: `await File.ReadAllTextAsync()`

Critical for high-traffic applications with database/API dependencies.

</details>

## 🛡️ Security Best Practices

### 22. What security headers should ASP.NET Core applications include?

<details>
<summary>🤔 Click to reveal answer</summary>

Essential security headers:
- **HSTS**: Force HTTPS connections
- **X-Frame-Options**: Prevent clickjacking
- **X-Content-Type-Options**: Prevent MIME sniffing
- **X-XSS-Protection**: Enable browser XSS filtering
- **CSP**: Content Security Policy against XSS
- **Referrer-Policy**: Control referrer information

Use security header middleware or configure manually.

</details>

### 23. How does CSRF protection work in ASP.NET Core?

<details>
<summary>🤔 Click to reveal answer</summary>

Anti-forgery token system:
1. **Token generation**: Server generates unique token per form
2. **Token inclusion**: Hidden field in HTML forms
3. **Token validation**: `[ValidateAntiForgeryToken]` validates token
4. **Automatic**: Razor forms include tokens automatically
5. **AJAX support**: Include tokens in AJAX requests

Protects against Cross-Site Request Forgery attacks.

</details>

### 24. What is Content Security Policy (CSP)?

<details>
<summary>🤔 Click to reveal answer</summary>

HTTP header that controls which resources browsers can load:
- **Script sources**: Whitelist JavaScript sources
- **Style sources**: Control CSS loading
- **Image sources**: Restrict image origins
- **Inline blocking**: Prevent inline scripts/styles
- **Reporting**: Get reports of policy violations

Powerful defense against XSS and code injection attacks.

</details>

## 🏗️ Configuration and Environment Management

### 25. How does the configuration system work in ASP.NET Core?

<details>
<summary>🤔 Click to reveal answer</summary>

Hierarchical configuration from multiple sources:
1. **appsettings.json**: Base configuration
2. **appsettings.{Environment}.json**: Environment-specific
3. **Environment variables**: System and process variables
4. **Command line**: Arguments passed to application
5. **User secrets**: Development-time secrets
6. **Azure Key Vault**: Production secrets management

Later sources override earlier ones.

</details>

### 26. What is the Options pattern?

<details>
<summary>🤔 Click to reveal answer</summary>

Strongly-typed configuration binding:
```csharp
public class DatabaseOptions
{
    public string ConnectionString { get; set; }
    public int CommandTimeout { get; set; }
}

services.Configure<DatabaseOptions>(Configuration.GetSection("Database"));
```

Access via `IOptions<DatabaseOptions>` in controllers/services.
Provides type safety and validation for configuration.

</details>

### 27. How do you manage different environments (Development, Staging, Production)?

<details>
<summary>🤔 Click to reveal answer</summary>

**Environment detection**: `ASPNETCORE_ENVIRONMENT` variable
- **Development**: Debug info, detailed errors, hot reload
- **Staging**: Production-like but with testing tools
- **Production**: Optimized, minimal logging, error pages

**Configuration**: Different appsettings files, services, and middleware per environment.

</details>

## 📊 Logging and Monitoring

### 28. How does the logging system work in ASP.NET Core?

<details>
<summary>🤔 Click to reveal answer</summary>

Built-in logging framework with multiple providers:
- **Log levels**: Trace, Debug, Information, Warning, Error, Critical
- **Categories**: Namespace-based logger categories
- **Providers**: Console, Debug, EventSource, File, Cloud providers
- **Structured logging**: Support for structured log data
- **Filtering**: Configure what gets logged where

Inject `ILogger<T>` into services for logging.

</details>

### 29. What is Health Check and how do you implement it?

<details>
<summary>🤔 Click to reveal answer</summary>

Monitor application health and dependencies:
```csharp
services.AddHealthChecks()
    .AddDbContext<ApplicationDbContext>()
    .AddUrlGroup(new Uri("https://api.example.com"), "External API");

app.MapHealthChecks("/health");
```

**Checks**: Database connectivity, external services, disk space
**Responses**: Healthy, Degraded, Unhealthy status with details

</details>

## 🚀 Hosting and Deployment

### 30. What hosting models are available for ASP.NET Core?

<details>
<summary>🤔 Click to reveal answer</summary>

- **In-process**: Hosted inside IIS worker process (fastest)
- **Out-of-process**: Separate process with IIS as reverse proxy
- **Kestrel**: Cross-platform web server (can run standalone)
- **Docker**: Containerized deployment
- **Cloud services**: Azure App Service, AWS Elastic Beanstalk
- **Self-hosted**: Console application hosting

</details>

### 31. What is Kestrel and how does it relate to IIS?

<details>
<summary>🤔 Click to reveal answer</summary>

**Kestrel**: Built-in, cross-platform web server
- Fast, lightweight HTTP server
- Runs on all platforms
- Can run standalone or behind reverse proxy

**With IIS**: IIS acts as reverse proxy
- IIS handles static files, SSL, compression
- Kestrel handles dynamic content
- Best performance and feature combination on Windows

</details>

### 32. What are the key considerations for production deployment?

<details>
<summary>🤔 Click to reveal answer</summary>

**Performance**:
- Enable response compression and caching
- Use production-optimized builds
- Configure appropriate timeout values

**Security**:
- Use HTTPS everywhere
- Enable security headers
- Keep frameworks and dependencies updated

**Monitoring**:
- Implement health checks
- Configure structured logging
- Set up application performance monitoring

</details>

---

📖 **[Return to Wiki Home](Home)**

🎯 **[Back to Examinator](https://github.com/QRY91/examinator)**