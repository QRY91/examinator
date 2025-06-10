# 🚀 BookHaven Multi-Project Setup Guide

**Status**: ✅ Solution builds successfully  
**Build Time**: ~27 seconds (includes NuGet restore)  
**Projects**: 4 (MVC + OrderApi + Shared + IdentityServer)

## 🔧 **Quick Setup**

### **1. Open in Visual Studio**

```bash
# Open the solution file
BookHaven.sln
```

### **2. Build the Solution**

```bash
# Command line build
dotnet build BookHaven.sln

# Or use Visual Studio: Build → Build Solution (Ctrl+Shift+B)
```

### **3. Run Multiple Projects**

Set up multiple startup projects in Visual Studio:

1. Right-click solution → **Set Startup Projects**
2. Select **Multiple startup projects**
3. Set **Action** to **Start** for:
   - BookHaven.MVC
   - BookHaven.OrderApi
   - BookHaven.IdentityServer

### **4. Default URLs**

When running, expect these URLs:

- **MVC Web App**: `https://localhost:5001`
- **Order API**: `https://localhost:7001` + `/swagger`
- **Identity Server**: `https://localhost:6001`

---

## 📁 **Project Structure**

```
BookHaven/                     # Solution root
├── BookHaven.sln             # Solution file
├── .gitignore                # Excludes build artifacts
├── BookHaven.MVC/            # Main web application
│   ├── Program.cs            # Basic MVC setup + HttpClient
│   ├── appsettings.json      # MVC database config
│   └── [MVC structure]       # Controllers, Views, Models
├── BookHaven.OrderApi/       # Order management API
│   ├── Program.cs            # API setup + Swagger
│   ├── appsettings.json      # API database config
│   └── [API structure]       # Controllers, Models, Services
├── BookHaven.Shared/         # DTOs and contracts
│   ├── DTOs/                 # Order & Inventory DTOs
│   └── BookHaven.Shared.csproj
└── BookHaven.IdentityServer/ # Authentication service
    ├── Program.cs            # Basic IdentityServer setup
    ├── appsettings.json      # Identity database config
    └── [Identity structure]   # Configuration, Pages
```

---

## ⚠️ **Known Issues & Notes**

### **Duende IdentityServer Warning**

- ✅ **Expected**: Low severity vulnerability warning on Duende.IdentityServer 7.0.7
- ✅ **Safe for exam**: This is a demo/learning setup, warning is acceptable
- 🔄 **In production**: Update to latest version

### **Build Order**

- ✅ **Automatic**: Projects build in correct dependency order
- ✅ **Shared → API → MVC → Identity**: Dependencies handled properly

### **Database Separation**

Each project has its own database:

- **MVC**: `BookHavenMvcDb`
- **OrderApi**: `BookHavenOrderDb`
- **IdentityServer**: `BookHavenIdentityDb`

---

## 🎯 **For Development/Testing**

### **Safe to Build**

- ✅ `.gitignore` excludes all build artifacts
- ✅ Can run `dotnet build` without affecting repo
- ✅ No `bin/` or `obj/` folders will be committed

### **Ready for Extensions**

- ✅ HTTP Client configured for MVC → API communication
- ✅ Project references set up correctly
- ✅ Separate configuration files for each service
- ✅ Swagger enabled for API development

### **Template Foundation**

- ✅ Basic project structure established
- ✅ NuGet packages configured for each project type
- ✅ Ready for adding models, controllers, views
- ✅ Authentication integration points prepared

---

## 🚀 **Next Steps for Students**

1. **Study the project relationships** - understand how MVC calls OrderApi
2. **Add Entity Framework** - create DbContexts for each database
3. **Implement shared DTOs** - design contracts between services
4. **Create API controllers** - implement order management endpoints
5. **Build MVC controllers** - consume the API from web interface
6. **Configure authentication** - integrate IdentityServer with MVC and API

**This foundation demonstrates the multi-project patterns you'll need for complex exam scenarios! 💪**
