import React from "react";
import Card from "./Card";

function CardsSection() {
  const cards = [
    {
      title: "Responsive Design",
      description: "Easily adapt layouts using sm, md, lg breakpoints."
    },
    {
      title: "Utility First",
      description: "Write styling directly in class names."
    },
    {
      title: "Fast Development",
      description: "No need to write custom CSS."
    },
    {
      title: "Modern UI",
      description: "Build clean and beautiful layouts."
    }
  ];

  return (
    <section className="py-16 px-6 bg-white">
      <h2 className="text-3xl font-bold text-center mb-12">
        Features
      </h2>

      <div className="
        grid 
        grid-cols-1 
        sm:grid-cols-2 
        lg:grid-cols-4 
        gap-8
      ">
        {cards.map((card, index) => (
          <Card
            key={index}
            title={card.title}
            description={card.description}
          />
        ))}
      </div>
    </section>
  );
}

export default React.memo(CardsSection);