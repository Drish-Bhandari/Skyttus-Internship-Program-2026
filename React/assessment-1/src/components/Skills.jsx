function Skills() {
  const skills = [
    "ReactJS",
    "Python",
    "Machine Learning",
    "Power BI",
    "SQL",
    "Django",
    "ASP.NET",
  ];

  return (
    <section id="skills" className="section">
      <h2>Skills</h2>
      <div className="skills-container">
        {skills.map((skill, index) => (
          <div key={index} className="skill-card">
            {skill}
          </div>
        ))}
      </div>
    </section>
  );
}

export default Skills;
