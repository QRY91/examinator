using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using BookHaven.Shared.Models;

namespace BookHaven.MVC.Data
{
    public class BookHavenDbContext : IdentityDbContext
    {
        public BookHavenDbContext(DbContextOptions<BookHavenDbContext> options) : base(options)
        {
        }

        public DbSet<Book> Books { get; set; }
        public DbSet<Author> Authors { get; set; }
        public DbSet<Category> Categories { get; set; }
        public DbSet<Customer> Customers { get; set; }
        public DbSet<Order> Orders { get; set; }
        public DbSet<OrderItem> OrderItems { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            // Configure relationships
            modelBuilder.Entity<Book>()
                .HasOne(b => b.Author)
                .WithMany(a => a.Books)
                .HasForeignKey(b => b.AuthorId);

            modelBuilder.Entity<Book>()
                .HasOne(b => b.Category)
                .WithMany(c => c.Books)
                .HasForeignKey(b => b.CategoryId);

            modelBuilder.Entity<Order>()
                .HasOne(o => o.Customer)
                .WithMany(c => c.Orders)
                .HasForeignKey(o => o.CustomerId);

            modelBuilder.Entity<OrderItem>()
                .HasOne(oi => oi.Order)
                .WithMany(o => o.OrderItems)
                .HasForeignKey(oi => oi.OrderId);

            modelBuilder.Entity<OrderItem>()
                .HasOne(oi => oi.Book)
                .WithMany(b => b.OrderItems)
                .HasForeignKey(oi => oi.BookId);

            // Seed data
            modelBuilder.Entity<Category>().HasData(
                new Category { Id = 1, Name = "Fiction", Description = "Fiction books", DisplayOrder = 1 },
                new Category { Id = 2, Name = "Non-Fiction", Description = "Non-fiction books", DisplayOrder = 2 },
                new Category { Id = 3, Name = "Science", Description = "Science books", DisplayOrder = 3 },
                new Category { Id = 4, Name = "History", Description = "History books", DisplayOrder = 4 },
                new Category { Id = 5, Name = "Biography", Description = "Biography books", DisplayOrder = 5 }
            );

            modelBuilder.Entity<Author>().HasData(
                new Author { Id = 1, FirstName = "J.K.", LastName = "Rowling", Biography = "British author, best known for the Harry Potter series" },
                new Author { Id = 2, FirstName = "Stephen", LastName = "King", Biography = "American writer of horror, supernatural fiction, suspense, crime, science-fiction, and fantasy novels" },
                new Author { Id = 3, FirstName = "Neil", LastName = "Gaiman", Biography = "English author of short fiction, novels, comic books, graphic novels, nonfiction, audio theatre, and films" },
                new Author { Id = 4, FirstName = "Isaac", LastName = "Asimov", Biography = "American writer and professor of biochemistry, known for his works of science fiction and popular science" },
                new Author { Id = 5, FirstName = "Agatha", LastName = "Christie", Biography = "English writer known for her sixty-six detective novels and fourteen short story collections" }
            );

            modelBuilder.Entity<Book>().HasData(
                new Book { Id = 1, Title = "Harry Potter and the Philosopher's Stone", Description = "A young wizard's first adventure", ISBN = "978-0747532699", Price = 19.99m, StockQuantity = 50, PublishedDate = new DateTime(1997, 6, 26), AuthorId = 1, CategoryId = 1 },
                new Book { Id = 2, Title = "The Shining", Description = "A family's stay at an isolated hotel takes a sinister turn", ISBN = "978-0307743657", Price = 24.99m, StockQuantity = 30, PublishedDate = new DateTime(1977, 1, 28), AuthorId = 2, CategoryId = 1 },
                new Book { Id = 3, Title = "Good Omens", Description = "A humorous take on the apocalypse", ISBN = "978-0060853983", Price = 22.50m, StockQuantity = 25, PublishedDate = new DateTime(1990, 5, 1), AuthorId = 3, CategoryId = 1 },
                new Book { Id = 4, Title = "Foundation", Description = "The first book in the Foundation series", ISBN = "978-0553293357", Price = 18.99m, StockQuantity = 40, PublishedDate = new DateTime(1951, 1, 1), AuthorId = 4, CategoryId = 3 },
                new Book { Id = 5, Title = "Murder on the Orient Express", Description = "A classic Hercule Poirot mystery", ISBN = "978-0062693662", Price = 16.99m, StockQuantity = 35, PublishedDate = new DateTime(1934, 1, 1), AuthorId = 5, CategoryId = 1 }
            );
        }
    }
} 