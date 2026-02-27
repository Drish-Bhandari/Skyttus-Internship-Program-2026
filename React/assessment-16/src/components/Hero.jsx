import React from "react";

function Hero() {
  return (
    <section className="bg-gray-100 py-16 px-6 text-center">
      <h2 className="text-3xl sm:text-4xl md:text-5xl font-bold mb-6">
        Build Responsive UI with Tailwind
      </h2>

      <p className="text-gray-600 max-w-2xl mx-auto mb-8">
        Tailwind CSS makes responsive design simple using utility classes.
        This layout adjusts beautifully across all devices.
      </p>

      <button className="bg-indigo-600 text-white px-6 py-3 rounded-lg hover:bg-indigo-700 transition">
        Get Started
      </button>
    </section>
  );
}

export default React.memo(Hero);