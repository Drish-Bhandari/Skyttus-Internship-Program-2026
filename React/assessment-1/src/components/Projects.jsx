import ProjectCard from "./ProjectCard";

import creditcard from "../assets/projects/creditcard.png";
import amazon from "../assets/projects/amazon.png";
import bookstore from "../assets/projects/bookstore.png";
import covid from "../assets/projects/covid.png";

function Projects() {
  const projectData = [
    {
      title: "Credit Card Financial Dashboard",
      description:
        "Interactive Power BI dashboard analyzing customer spending behavior, revenue trends, and transaction insights using DAX and data modeling.",
      image: creditcard,
      tech: "Power BI | DAX | Data Modeling",
    },
    {
      title: "Amazon Sales Dashboard",
      description:
        "Data analytics dashboard visualizing Amazon sales performance, product trends, and customer insights with dynamic filters.",
      image: amazon,
      tech: "Power BI | Excel | Data Cleaning",
    },
    {
      title: "Online Book Store SQL System",
      description:
        "Relational database design with 10+ tables, business queries, joins, triggers and normalization for managing books, orders, and customers.",
      image: bookstore,
      tech: "PostgreSQL | SQL | Database Design",
    },
    {
      title: "COVID-19 Data Analysis",
      description:
        "Python-based exploratory data analysis and visualization of global COVID-19 trends using Pandas and Matplotlib.",
      image: covid,
      tech: "Python | Pandas | Matplotlib",
    },
  ];

  return (
    <section id="projects" className="section">
      <h2>Projects</h2>

      <div className="projects-container">
        {projectData.map((project, index) => (
          <ProjectCard
            key={index}
            title={project.title}
            description={project.description}
            image={project.image}
            tech={project.tech}
          />
        ))}
      </div>
    </section>
  );
}

export default Projects;
