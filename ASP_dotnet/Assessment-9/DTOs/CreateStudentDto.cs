using System.ComponentModel.DataAnnotations;

namespace StudentApi.DTOs
{
    public class CreateStudentDTO
    {
        [Required]
        public string Name { get; set; }

        [Required]
        public string Department { get; set; }

        public int Marks { get; set; }
    }
}
