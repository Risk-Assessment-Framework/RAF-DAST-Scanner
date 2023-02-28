import { React, Fragment, useEffect, useState } from "react";
import {
  ExclamationCircleIcon,
  ChevronDownIcon,
} from "@heroicons/react/20/solid";
import { Menu, Transition } from "@headlessui/react";
import { baseUrl } from "../configs/api-config";

function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}

export default function Reports(props) {
  const [scanResults, setScanResults] = useState([]);
  const [scanStatus, setScanStatus] = useState(false);
  const url = props.url;
  console.log(url);
  const data = { url: url, ascan: false };
  let results;
  const riskValues = {
    Low: 1,
    Medium: 2,
    High: 3,
  };

  useEffect(() => {
    const fetchScanResults = async () => {
      const response = await fetch(`${baseUrl}/spider`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      results = await response.json();
      results = results["Scan Results"]["alerts"];
      if (results.length === 0) {
        setScanResults([]);
        setScanStatus(false);
        return;
      }
      results = results.filter((result) => result.risk !== "Informational");
      results = results.sort(function (a, b) {
        return riskValues[b.risk] - riskValues[a.risk];
      });
      console.log(results);
      setScanResults(results);
      setScanStatus(true);
    };

    fetchScanResults();
  }, []);

  return !scanStatus ? (
    <div class="bg-white p-2 sm:p-4 sm:h-64 rounded-2xl shadow-lg flex flex-col sm:flex-row gap-5 select-none ">
      <div class="h-52 sm:h-full sm:w-72 rounded-xl bg-gray-200 animate-pulse"></div>
      <div class="flex flex-col flex-1 gap-5 sm:p-2">
        <div class="flex flex-1 flex-col gap-3">
          <div class="bg-gray-200 w-full animate-pulse h-14 rounded-2xl"></div>
          <div class="bg-gray-200 w-full animate-pulse h-3 rounded-2xl"></div>
          <div class="bg-gray-200 w-full animate-pulse h-3 rounded-2xl"></div>
          <div class="bg-gray-200 w-full animate-pulse h-3 rounded-2xl"></div>
          <div class="bg-gray-200 w-full animate-pulse h-3 rounded-2xl"></div>
        </div>
        <div class="mt-auto flex gap-3">
          <div class="bg-gray-200 w-20 h-8 animate-pulse rounded-full"></div>
          <div class="bg-gray-200 w-20 h-8 animate-pulse rounded-full"></div>
          <div class="bg-gray-200 w-20 h-8 animate-pulse rounded-full ml-auto"></div>
        </div>
      </div>
    </div>
  ) : (
    <div className="overflow-hidden bg-white shadow sm:rounded-md rounded-md">
      <ul role="list" className="divide-y divide-gray-200">
        {scanResults.map((position) => (
          <li key={position.id}>
            <Menu as="div" className="block hover:bg-gray-50">
              <Menu.Button className="px-4 py-4 sm:px-6 w-full">
                <div className="flex items-center justify-between">
                  <p className="truncate text-sm font-medium text-indigo-600">
                    {position.name}
                  </p>
                  <div className="ml-2 flex flex-shrink-0">
                    <p
                      className={`inline-flex rounded-full ${
                        position.risk === "High"
                          ? "bg-red-100 text-red-800"
                          : position.type === "Medium"
                          ? "bg-yellow-100 text-yellow-800"
                          : "bg-green-100 text-green-800"
                      }  px-2 text-xs font-semibold leading-5 `}
                    >
                      {position.risk}
                    </p>
                  </div>
                </div>
                <div className="mt-2 flex items-center justify-between sm:flex sm:justify-between">
                  <div className="sm:flex">
                    <p className="flex items-center text-sm text-gray-500">
                      <ExclamationCircleIcon
                        className="mr-1.5 h-5 w-5 flex-shrink-0 text-gray-400"
                        aria-hidden="true"
                      />
                      {/* {position.category} */}
                      {`CWE ID: ${position.cweid}`}
                    </p>
                  </div>

                  <div className="mt-2 flex items-center text-sm text-gray-500 sm:mt-0">
                    <ChevronDownIcon
                      className="mr-1.5 h-5 w-5 flex-shrink-0 text-gray-400"
                      aria-hidden="true"
                    />
                  </div>
                </div>
              </Menu.Button>

              <Transition
                as={Fragment}
                enter="transition ease-out duration-100"
                enterFrom="transform opacity-0 scale-95"
                enterTo="transform opacity-100 scale-100"
                leave="transition ease-in duration-75"
                leaveFrom="transform opacity-100 scale-100"
                leaveTo="transform opacity-0 scale-95"
              >
                <Menu.Items className="px-4 py-4 sm:px-6 origin-top-right divide-y divide-gray-100 rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                  <a
                    href="#"
                    className="-m-3 block rounded-md p-4 transition duration-150 ease-in-out hover:bg-gray-50"
                  >
                    <p className="text-base font-medium text-gray-900">
                      {"Description"}
                    </p>
                    <p className="mt-1 mb-2 text-sm text-gray-500">
                      {position.description}
                    </p>
                  </a>
                  <a
                    href={position.reference}
                    target="_blank"
                    className="-m-3 block rounded-md p-3 transition duration-150 ease-in-out hover:bg-gray-50"
                  >
                    <p className="text-base font-medium text-gray-900">
                      {"Solution"}
                    </p>
                    <p className="mt-1 text-sm text-gray-500">
                      {position.solution}
                    </p>
                  </a>
                </Menu.Items>
              </Transition>
            </Menu>
          </li>
        ))}
      </ul>
    </div>
  );
}
