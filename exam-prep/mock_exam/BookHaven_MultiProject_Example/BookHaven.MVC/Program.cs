using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using BookHaven.MVC.Data;

var builder = WebApplication.CreateBuilder(args);

// Add Entity Framework and Identity services
var connectionString = builder.Configuration.GetConnectionString("DefaultConnection") ?? throw new InvalidOperationException("Connection string 'DefaultConnection' not found.");
builder.Services.AddDbContext<BookHavenDbContext>(options =>
    options.UseSqlServer(connectionString));

builder.Services.AddDefaultIdentity<IdentityUser>(options => options.SignIn.RequireConfirmedAccount = false)
    .AddEntityFrameworkStores<BookHavenDbContext>();

// Add services to the container.
builder.Services.AddControllersWithViews();

// Add HttpClient for API communication
var apiUrl = builder.Configuration["ApiSettings:OrderApiUrl"] ?? "https://localhost:7001";
builder.Services.AddHttpClient("OrderApi", client =>
{
    client.BaseAddress = new Uri(apiUrl);
});

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthentication();
app.UseAuthorization();

app.MapRazorPages();
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run(); 