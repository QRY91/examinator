# 🃏 Brixeluser - LLM Generated Flashcards
*Generated from: BrixelUser.cs*

1. **What is IdentityUser in ASP.NET Core**: It's a built-in class provided by Microsoft for managing user authentication and authorization in an application.
2. **What does the CustomerId property represent in BrixelUser class**: It represents the ID of a customer profile associated with a user, but its nullable because not every user needs to have a customer profile.
3. **What is the purpose of the private constructor in BrixelUser class**: It's used to prevent instantiation of this class directly and force use of the provided public constructor.
4. **How does the public constructor of BrixelUser initialize the base class IdentityUser**: It initializes the base class IdentityUser with a username parameter.
5. **What is the role of the BrixelUser class in Webshop.MVC application**: It extends the IdentityUser class to add an association between users and customer profiles, allowing for both customer and admin/employee user types.
6. **Why is the CustomerId property nullable**: Because not all users will have a customer profile associated with them.
7. **What is the effect of having a null CustomerId value**: It indicates that the user does not have an associated customer profile.
8. **What is the purpose of using a nullable int for the CustomerId property**: Using a nullable int allows for the representation of both existing customer IDs and the absence of a customer profile by storing null.
9. **What happens when you try to access or assign a non-nullable int to the CustomerId property**: You will encounter a compile-time error because the property is declared as nullable.
10. **How can you check if a BrixelUser has an associated customer profile**: By checking if the CustomerId property has a value (i.e., not null).
11. **What is the difference between a regular user and a customer user in this context**: A regular user doesn't have a customer profile, while a customer user has an associated customer profile.
12. **What is the primary function of the built-in IdentityUser class**: Managing user authentication and authorization within an ASP.NET Core application.
13. **What is the role of the BrixelUser constructor with no parameters**: It creates an instance of BrixelUser without initializing any properties, making it useful for inheritance or complex object creation scenarios.
14. **What is a nullable type in C#**: A nullable type is a value type that can hold a null value in addition to its regular values. In the example, int? is a nullable integer.
15. **Why use inheritance with IdentityUser and BrixelUser classes**: To extend the functionality of the base class (IdentityUser) by adding custom properties or behavior while maintaining compatibility with existing methods and interfaces.