import React from "react";
import Navbar from "../components/Navbar";
import { people, auditHistoryData } from "../mock/dashboard-data";
import { EyeIcon, TrashIcon } from "@heroicons/react/20/solid";

const History = () => {
  return (
    <div className="min-h-full">
      <div className="bg-gray-800 pb-32">
        <Navbar />

        <header className="py-10">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <h1 className="text-3xl font-bold tracking-tight text-white">
              {auditHistoryData.title}
            </h1>
          </div>
        </header>
      </div>

      <main className="-mt-32">
        <div className="mx-auto max-w-7xl px-4 pb-12 sm:px-6 lg:px-8">
          <div className="rounded-lg bg-white px-5 py-6 shadow sm:px-6">
            {/* <div className="h-76 rounded-lg border-4 border-dashed border-gray-200 "> */}
            <div className="bg-white">
              <div className="px-4 sm:px-6 lg:px-8">
                <div className="sm:flex sm:items-center">
                  <div className="sm:flex-auto">
                    <h1 className="text-base font-semibold leading-6 text-gray-900">
                      Scan History
                    </h1>
                    {/* <p className="mt-2 text-sm text-gray-700">
                      A list of all the users in your account including their
                      name, title, email and role.
                    </p> */}
                  </div>
                  {/* <div className="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
                    <button
                      type="button"
                      className="block rounded-md bg-indigo-600 py-2 px-3 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                    >
                      Add user
                    </button>
                  </div> */}
                </div>
                <div className="mt-8 flow-root">
                  <div className="-my-2 -mx-4 overflow-x-auto sm:-mx-6 lg:-mx-8">
                    <div className="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
                      <div className="overflow-hidden shadow ring-1 ring-black ring-opacity-5 sm:rounded-lg">
                        <table className="min-w-full divide-y divide-gray-300">
                          <thead className="bg-gray-50">
                            <tr>
                              <th
                                scope="col"
                                className="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6"
                              >
                                Website
                              </th>
                              <th
                                scope="col"
                                className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                              >
                                Scan #
                              </th>
                              <th
                                scope="col"
                                className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                              >
                                Status
                              </th>
                              <th
                                scope="col"
                                className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                              >
                                Created At
                              </th>
                              <th
                                scope="col"
                                className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                              >
                                Updated At
                              </th>
                              <th
                                scope="col"
                                className="relative py-3.5 pl-3 pr-4 sm:pr-6"
                              >
                                <span className="sr-only">Edit</span>
                              </th>
                            </tr>
                          </thead>
                          <tbody className="divide-y divide-gray-200 bg-white">
                            {people.map((person) => (
                              <tr key={person.email}>
                                <td className="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6">
                                  {person.website}
                                </td>
                                <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                                  {person.number}
                                </td>
                                <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                                  {person.status}
                                </td>
                                <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                                  {person.createdAt}
                                </td>
                                <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                                  {person.updatedAt}
                                </td>
                                <td className="relative whitespace-nowrap py-4 text-right text-sm font-medium sm:pr-6">
                                  <div className="flex space-x-4">
                                    <div className="flex">
                                      <a
                                        href="#"
                                        className="-m-2 p-2 text-gray-400 hover:text-gray-500"
                                      >
                                        <span className="sr-only">Search</span>
                                        <EyeIcon
                                          className="h-6 w-6"
                                          aria-hidden="true"
                                        />
                                      </a>
                                    </div>

                                    <div className="flex">
                                      <a
                                        href="#"
                                        className="-m-2 p-2 text-gray-400 hover:text-gray-500"
                                      >
                                        <span className="sr-only">Account</span>
                                        <TrashIcon
                                          className="h-6 w-6"
                                          aria-hidden="true"
                                        />
                                      </a>
                                    </div>
                                  </div>
                                </td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default History;
