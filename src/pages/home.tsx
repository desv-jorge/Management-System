import Header from "../components/header";
import ServiceDashboard from "../components/Home/ServiceDashboard";

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-200 font-sans">
      <Header />

      <main className="px-4 sm:px-6 lg:px-8 py-6">
        <h1 className="text-2xl sm:text-3xl lg:text-4xl font-bold mb-6 text-center sm:text-left">
          Dashboards
        </h1>

        <div className="flex flex-col gap-6">
          <ServiceDashboard />
        </div>
      </main>
    </div>
  );
}
