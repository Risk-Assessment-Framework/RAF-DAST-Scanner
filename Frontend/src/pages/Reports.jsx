import { React, Fragment } from "react";
import {
  BugAntIcon,
  MapPinIcon,
  ExclamationCircleIcon,
  ChevronDownIcon,
} from "@heroicons/react/20/solid";
import { Menu, Transition } from "@headlessui/react";
import { auditData } from "../mock/dashboard-data";

function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}

export default function Reports() {
  return (
    <div className="overflow-hidden bg-white shadow sm:rounded-md rounded-md">
      <ul role="list" className="divide-y divide-gray-200">
        {auditData.map((position) => (
          <li key={position.id}>
            <Menu as="div" className="block hover:bg-gray-50">
              <Menu.Button className="px-4 py-4 sm:px-6 w-full">
                <div className="flex items-center justify-between">
                  <p className="truncate text-sm font-medium text-indigo-600">
                    {position.title}
                  </p>
                  <div className="ml-2 flex flex-shrink-0">
                    <p
                      className={`inline-flex rounded-full ${
                        position.type === "High"
                          ? "bg-red-100 text-red-800"
                          : position.type === "Medium"
                          ? "bg-yellow-100 text-yellow-800"
                          : "bg-green-100 text-green-800"
                      }  px-2 text-xs font-semibold leading-5 `}
                    >
                      {position.type}
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
                      {position.category}
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
                  {position.solutions.map((item) => (
                    <a
                      key={item.name}
                      href={item.href}
                      className="-m-3 block rounded-md p-3 transition duration-150 ease-in-out hover:bg-gray-50"
                    >
                      <p className="text-base font-medium text-gray-900">
                        {item.name}
                      </p>
                      <p className="mt-1 text-sm text-gray-500">
                        {item.description}
                      </p>
                    </a>
                  ))}
                </Menu.Items>
              </Transition>
            </Menu>
          </li>
        ))}
      </ul>
    </div>
  );
}
