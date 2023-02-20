import React from "react";
import Navbar from "../components/Navbar";
import { dashboardData } from "../mock/dashboard-data";
import Reports from "./Reports";
import { useSearchParams } from "react-router-dom";

const Dashboard = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  return (
    <div className="min-h-full">
      <div className="bg-gray-800 pb-32">
        <Navbar />

        <header className="py-10">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <h1 className="text-3xl font-bold tracking-tight text-white">
              {dashboardData.title}
            </h1>
          </div>
        </header>
      </div>

      <main className="-mt-32">
        <div className="mx-auto max-w-7xl px-4 pb-12 sm:px-6 lg:px-8">
          {/* Replace with your content */}
          <div className="rounded-lg bg-white px-5 py-6 shadow sm:px-6">
            <div className="h-76 rounded-lg border-4 border-dashed border-gray-200 ">
              <div className="bg-white">
                <div className="mx-auto max-w-7xl py-12 px-6 lg:py-12 lg:px-8">
                  <h2 className="inline text-2xl font-bold tracking-tight text-gray-900 sm:block sm:text-3xl">
                    Showing results for
                  </h2>
                  <div>
                    <p className="text-2xl font-bold tracking-tight truncate sm:truncate text-indigo-600 sm:block sm:text-3xl">
                      {searchParams.get("site")
                        ? searchParams.get("site").toLowerCase()
                        : dashboardData.domain}
                    </p>
                  </div>
                  <p className="text-sm font-medium leading-4 md:leading-8 text-neutral-600 sm:text-base">
                    Hosted at {dashboardData.ipv4} and {dashboardData.ipv6}
                  </p>
                  <form
                    className="mt-8 sm:flex"
                    action="/dashboard"
                    method="GET"
                  >
                    <input
                      type="text"
                      name="site"
                      id="site"
                      required
                      className="w-full rounded-md border-gray-300 px-5 py-3 placeholder-gray-500 focus:border-indigo-500 focus:ring-indigo-500 sm:max-w-xs"
                      placeholder="Enter your site URL"
                    />
                    <div className="mt-3 rounded-md shadow sm:mt-0 sm:ml-3 sm:flex-shrink-0">
                      <button
                        type="submit"
                        className="flex w-full items-center justify-center rounded-md border border-transparent bg-indigo-600 px-5 py-3 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                      >
                        Analyze
                      </button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>

          {/* Reports Section */}
          <div className="pt-4">
            <Reports />
          </div>

          {/* /End replace */}
        </div>
      </main>

      <div></div>
    </div>
  );
};

export default Dashboard;
