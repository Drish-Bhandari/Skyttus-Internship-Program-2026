using System;
using System.Collections.Generic;
using System.Linq;

class Student
{
    public int StudentId;
    public string Name;
    public string Department;
    public int Marks;
}

class Program
{
    static void Main()
    {
        List<Student> students = new List<Student>();

        // 1.Accept student details from user

        Console.Write("Enter number of students: ");
        int count = int.Parse(Console.ReadLine());

        for (int i = 0; i < count; i++)
        {
            Console.WriteLine($"\nEnter details for Student {i + 1}");

            Student s = new Student();

            Console.Write("Student ID: ");
            s.StudentId = int.Parse(Console.ReadLine());

            Console.Write("Name: ");
            s.Name = Console.ReadLine();

            Console.Write("Department: ");
            s.Department = Console.ReadLine();

            Console.Write("Marks: ");
            s.Marks = int.Parse(Console.ReadLine());

            students.Add(s);
        }

        int choice;

        do
        {
            Console.WriteLine("1. Display all student records");
            Console.WriteLine("2. Display name and department");
            Console.WriteLine("3. Students with marks > 75");
            Console.WriteLine("4. Students from specific department");
            Console.WriteLine("5. Sort students by marks (DESC)");
            Console.WriteLine("6. Display top scorer");
            Console.WriteLine("0. Exit");
            Console.Write("Enter your choice: ");

            choice = int.Parse(Console.ReadLine());

            switch (choice)
            {
                //2.Display all student records
                case 1:
                    Console.WriteLine("\nAll Student Records:");
                    foreach (var s in students)
                    {
                        Console.WriteLine($"{s.StudentId} | {s.Name} | {s.Department} | {s.Marks}");
                    }
                    break;

                // 3.Display only Name and Department
                case 2:
                    Console.WriteLine("\nName and Department:");
                    foreach (var s in students)
                    {
                        Console.WriteLine($"{s.Name} - {s.Department}");
                    }
                    break;
                
                // 4.Students with marks > 75
                case 3:
                    Console.WriteLine("\nStudents with Marks > 75:");
                    foreach (var s in students)
                    {
                        if (s.Marks > 75)
                        {
                            Console.WriteLine($"{s.Name} - {s.Marks}");
                        }
                    }
                    break;

                // 5.Students from specific department
                case 4:
                    Console.Write("\nEnter Department: ");
                    string dept = Console.ReadLine();

                    Console.WriteLine("\nStudents from Department:");
                    foreach (var s in students)
                    {
                        if (s.Department.Equals(dept, StringComparison.OrdinalIgnoreCase))
                        {
                            Console.WriteLine($"{s.Name} - {s.Department}");
                        }
                    }
                    break;
                    
                // 6.Sort students by marks DESC
                case 5:
                    Console.WriteLine("\nStudents Sorted by Marks (DESC):");

                    var sortedList = students
                        .OrderByDescending(s => s.Marks);

                    foreach (var s in sortedList)
                    {
                        Console.WriteLine($"{s.Name} - {s.Marks}");
                    }
                    break;

                // 7.Display Top Scorer
                case 6:
                    int maxMarks = students.Max(s => s.Marks);

                    Console.WriteLine("\nTop Scorer:");
                    foreach (var s in students)
                    {
                        if (s.Marks == maxMarks)
                        {
                            Console.WriteLine($"{s.Name} - {s.Marks}");
                        }
                    }
                    break;

                case 0:
                    Console.WriteLine("Exiting program...");
                    break;

                default:
                    Console.WriteLine("Invalid choice!");
                    break;
            }

        } while (choice != 0);
    }
}
