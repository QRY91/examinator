# School Laptop Workflow Test: 30-Minute Verification

**Purpose**: Verify exam prep materials work correctly on your exam device  
**Time Required**: 30 minutes total  
**Goal**: Confidence that templates and strategy work on your specific setup  
**Run This**: Night before exam or morning of (not during exam time)

---

## 🎯 **OVERVIEW: What We're Testing**

- **Template copy-paste speed** - Can you use them efficiently?
- **Find/replace workflow** - Does placeholder replacement work smoothly?
- **Basic project creation** - Can you set up a project in 15 minutes?
- **Your development environment** - Any school laptop specific issues?
- **Timing accuracy** - Are the time estimates realistic for you?

---

## ⏱️ **TEST SCHEDULE (Set Timers!)**

| Test Phase | Time Limit | What You're Testing |
|------------|------------|-------------------|
| **Setup Test** | 0-5 min | Basic project creation |
| **Template Test** | 5-15 min | Copy-paste workflow |
| **CRUD Test** | 15-25 min | Basic functionality |
| **Debrief** | 25-30 min | Notes and adjustments |

**Total**: 30 minutes - Set timer for each phase!

---

## 🚀 **PHASE 1: SETUP TEST (0-5 minutes)**

### **Goal**: Verify basic project creation works
**Timer**: Set 5-minute countdown

### **Steps**:
1. **Open terminal/command prompt**
2. **Create test project**:
   ```bash
   dotnet new mvc -n ExamTest
   cd ExamTest
   dotnet add package Microsoft.AspNetCore.Identity.EntityFrameworkCore
   dotnet add package Microsoft.EntityFrameworkCore.SqlServer
   dotnet add package Microsoft.EntityFrameworkCore.Tools
   ```
3. **Open in Visual Studio/VS Code**
4. **Run the project** (`dotnet run` or F5)
5. **Verify** default MVC page loads in browser

### **Success Criteria**:
- [ ] Project created without errors
- [ ] All packages installed successfully
- [ ] Project runs and shows default MVC page
- [ ] No compiler errors

### **If This Fails**: Stop here - fix development environment before exam

---

## 📋 **PHASE 2: TEMPLATE TEST (5-15 minutes)**

### **Goal**: Test copy-paste and find/replace workflow
**Timer**: Set 10-minute countdown

### **Steps**:
1. **Copy Model template**:
   - Open `templates/Model.cs.template`
   - Copy entire content
   - Create `Models/Product.cs`
   - Paste content

2. **Test find/replace**:
   - Find: `{ProjectName}` → Replace: `ExamTest`
   - Find: `{Entity}` → Replace: `Product`
   - Find: `{Entities}` → Replace: `Products`
   - Find: `{RelatedEntity}` → Replace: `Category`
   - Find: `{RelatedEntities}` → Replace: `Categories`

3. **Create Category model**:
   - Copy template again
   - Create `Models/Category.cs`
   - Replace placeholders with Category/Categories

4. **Check syntax**:
   - Build project (`dotnet build`)
   - Fix any syntax errors

### **Success Criteria**:
- [ ] Templates copy-paste cleanly
- [ ] Find/replace works efficiently
- [ ] Models compile without syntax errors
- [ ] Can complete in under 10 minutes

### **Time Check**: If over 10 minutes, practice find/replace more

---

## 🗄️ **PHASE 3: CRUD TEST (15-25 minutes)**

### **Goal**: Test full template workflow
**Timer**: Set 10-minute countdown

### **Steps**:
1. **Create DbContext** (3 minutes):
   - Copy `templates/DbContext.cs.template`
   - Create `Data/ExamTestDbContext.cs`
   - Replace placeholders
   - Add connection string to `appsettings.json`:
     ```json
     {
       "ConnectionStrings": {
         "DefaultConnection": "Server=(localdb)\\mssqllocaldb;Database=ExamTestDb;Trusted_Connection=true;MultipleActiveResultSets=true"
       }
     }
     ```

2. **Update Program.cs** (2 minutes):
   - Copy relevant sections from `templates/Program.cs.template`
   - Add DbContext registration
   - Add basic services

3. **Create Migration** (2 minutes):
   - `Add-Migration InitialCreate`
   - `Update-Database`

4. **Test Database** (3 minutes):
   - Run project
   - Verify no database errors
   - Check that database was created

### **Success Criteria**:
- [ ] DbContext created correctly
- [ ] Migration runs successfully
- [ ] Database creates without errors
- [ ] Project runs with database integration
- [ ] Completed in under 10 minutes

### **Critical**: If migration fails, this will block you in exam - practice until it works

---

## 📝 **PHASE 4: DEBRIEF (25-30 minutes)**

### **Goal**: Document what works and what needs adjustment

### **Questions to Answer**:
1. **What took longer than expected?**
2. **Which templates were hardest to use?**
3. **Any school laptop specific issues?**
4. **What would you change about the workflow?**
5. **Are you confident with the copy-paste speed?**

### **Adjustments to Make**:
- [ ] **If behind time**: Practice find/replace more
- [ ] **If syntax errors**: Review template placeholders
- [ ] **If migration issues**: Practice EF commands
- [ ] **If environment issues**: Fix before exam

### **Create Your Cheat Sheet**:
Write down:
- Any school laptop specific commands
- Shortcuts that work for you
- Common errors you encountered and fixes
- Your personal timing adjustments

---

## 🚨 **COMMON ISSUES & SOLUTIONS**

### **"Migration Failed"**
**Solution**: Check model syntax, ensure proper relationships
```bash
Remove-Migration
# Fix model issues
Add-Migration InitialCreate
```

### **"Package Not Found"**
**Solution**: Check internet connection, try different package source
```bash
dotnet nuget list source
dotnet restore
```

### **"Templates Don't Work"**
**Solution**: Check file encoding, ensure all placeholders replaced
- Copy one line at a time if full copy fails
- Use Notepad++ or VS Code for find/replace

### **"Too Slow"**
**Solution**: Practice specific workflows
- Focus on find/replace speed
- Use IDE shortcuts (Ctrl+H for find/replace)
- Practice typing common entity names

---

## ✅ **WORKFLOW VERIFICATION CHECKLIST**

### **After Completing Test**:
- [ ] **Templates copy-paste reliably**
- [ ] **Find/replace workflow is smooth**
- [ ] **Basic project setup works (under 15 minutes)**
- [ ] **Database creation succeeds**
- [ ] **No school laptop specific blockers**
- [ ] **Confident with timing estimates**
- [ ] **Know how to recover from common errors**

### **If ANY checklist item fails**: Practice that specific part more

---

## 🎯 **SUCCESS METRICS**

### **Minimum Success** (You're ready for exam):
- Complete test in 30 minutes
- No blocking technical issues
- Templates work on your setup
- Confident with basic workflow

### **Optimal Success** (You'll excel in exam):
- Complete test in 20 minutes
- Smooth copy-paste workflow
- Quick find/replace execution
- Know shortcuts and error recovery

---

## 🎓 **FINAL CONFIDENCE CHECK**

### **Ask Yourself**:
1. **"Can I create a basic project in 15 minutes?"**
2. **"Do the templates save me time vs writing from scratch?"**
3. **"Am I confident with the find/replace workflow?"**
4. **"Do I know how to recover from common errors?"**
5. **"Am I ready to help classmates if they have questions?"**

### **If YES to all**: You're ready! 🚀
### **If NO to any**: Practice that specific area more

---

## 📋 **NOTES SECTION**

**Use this space to write your observations:**

**What worked well:**
- 
- 
- 

**What needs more practice:**
- 
- 
- 

**School laptop specific notes:**
- 
- 
- 

**Timing adjustments:**
- 
- 
- 

**Personal shortcuts discovered:**
- 
- 
- 

---

## 🏆 **FINAL MESSAGE**

**Remember**: This test is about confidence, not perfection. You've built webshops before. The templates just help you do it faster under pressure.

**If the test goes well**: You're ready to share with classmates and ace the exam.

**If the test reveals issues**: Better to find them now than during the exam.

**You got this! The systematic approach works.** 🚀

---

**Next Steps After Test**:
1. **Share with classmates** (if test went well)
2. **Get good sleep** 
3. **Light review** of templates tomorrow morning
4. **Execute systematically** during exam