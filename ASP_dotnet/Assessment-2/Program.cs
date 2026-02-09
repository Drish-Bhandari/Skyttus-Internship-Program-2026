using System;
using System.Collections.Generic;
using System.Linq;

// 1: Create Student Class
class Student
{
    private int studentId;
    private string name;
    private string department;
    private int year;
    private int marks;

    // 2: Use constructor to initialize values
    public Student(int studentId, string name, string department, int year, int marks)
    {
        this.studentId = studentId;
        this.name = name;
        this.department = department;
        this.year = year;
        this.marks = marks;
    }

    // 3: Apply encapsulation (get/set)
    public int StudentId
    {
        get { return studentId; }
        set { studentId = value; }
    }
    public string Name
    {
        get { return name; }
        set { name = value; }
    }
    public string Department
    {
        get { return department; }
        set { department = value; }
    }
    public int Year
    {
        get { return year; }
        set { year = value; }
    }
    public int Marks
    {
        get { return marks; }
        set { marks = value; }
    }
}
class Program
{
    static void Main()
    {
        // 4: Create multiple student objects
        List<Student> students = new List<Student>
        {
            new Student(1, "Drish", "IT", 4, 82),
            new Student(2, "Preet", "CS", 2, 74),
            new Student(3, "Meet", "IT", 3, 91),
            new Student(4, "Kirtan", "EC", 1, 88),
            new Student(5, "Jay", "CS", 4, 79)
        };

        // 5: Display all student records
        Console.WriteLine("All Student Records:");
        foreach (var s in students)
        {
            Console.WriteLine($"{s.StudentId} | {s.Name} | {s.Department} | Year {s.Year} | Marks {s.Marks}");
        }

        // 6: Students with marks > 75
        Console.WriteLine("\nStudents with Marks > 75:");
        var highScorers = students.Where(s => s.Marks > 75);
        foreach (var s in highScorers)
        {
            Console.WriteLine($"{s.Name} - {s.Marks}");
        }

        // 7: Sort students by marks
        Console.WriteLine("\nStudents Sorted by Marks (Descending):");
        var sortedStudents = students.OrderByDescending(s => s.Marks);
        foreach (var s in sortedStudents)
        {
            Console.WriteLine($"{s.Name} - {s.Marks}");
        }

        // 8: Display top 3 scorers
        Console.WriteLine("\nTop 3 Scorers:");
        var topThree = students.OrderByDescending(s => s.Marks).Take(3);

        foreach (var s in topThree)
        {
            Console.WriteLine($"{s.Name} - {s.Marks}");
        }
    }
}

