using System.ComponentModel.DataAnnotations;

namespace EfRepoMvcApp.Models
{
    public class Student
    {
        public int Id { get; set; }

        [Required]
        public string Name { get; set; }

        [Required]
        public string Department { get; set; }

        public int Marks { get; set; }
    }
}
