export const demouser = {
  name: "Shubhayu Majumdar",
  email: "tom@example.com",
  imageUrl:
    "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
};
export const navigation = [
  { name: "Report", href: "#", current: true },
  { name: "Tools", href: "#", current: false },
  { name: "Resources", href: "#", current: false },
  { name: "Documentation", href: "#", current: false },
  { name: "Support", href: "#", current: false },
];
export const userNavigation = [
  // { name: "Your Profile", href: "#" },
  // { name: "Settings", href: "#" },
  { name: "Sign out", href: "#" },
];

export const homeNavigation = [
  { name: "Scanner Types", href: "#" },
  { name: "Documentation", href: "#" },
  { name: "Features", href: "#" },
];

export const dashboardData = {
  domain: "example.com",
  title: "Security Audit",
  ipv4: "216.239.38.117",
  ipv6: "2001:4860:4802:32::75",
};

export const auditData = [
  {
    id: 1,
    title: "X-XSS-Protection header set to 0 (disabled)",
    type: "High",
    category: "Header Security",
    solutions: [
      {
        name: "Description",
        description:
          'The x-xss-protection header is designed to enable the cross-site scripting (XSS) filter built into modern web browsers. Explicitly setting X-XSS-Protection header to "0" will allow an attacker to perform XSS attack on your users..',
        href: "#",
      },
      {
        name: "Remediation",
        description:
          "The recommended configuration is to set this header to the following value, which will enable the XSS protection and instruct the browser to block the response in the event that a malicious script has been inserted from user input, instead of sanitizing. x-xss-protection: 1; mode=block.",
        href: "#",
      },
    ],
  },
  {
    id: 2,
    title:
      "Cookies use SameSite flag, but set to something other than Strict or Lax",
    type: "Medium",
    category: "Cookie Security",
    solutions: [
      {
        name: "Description",
        description:
          'The x-xss-protection header is designed to enable the cross-site scripting (XSS) filter built into modern web browsers. Explicitly setting X-XSS-Protection header to "0" will allow an attacker to perform XSS attack on your users..',
        href: "#",
      },
      {
        name: "Remediation",
        description:
          "The recommended configuration is to set this header to the following value, which will enable the XSS protection and instruct the browser to block the response in the event that a malicious script has been inserted from user input, instead of sanitizing. x-xss-protection: 1; mode=block.",
        href: "#",
      },
    ],
  },
  {
    id: 3,
    title: "Content Security Policy (CSP) header not implemented",
    type: "Low",
    category: "Header Security",
    solutions: [
      {
        name: "Description",
        description:
          'The x-xss-protection header is designed to enable the cross-site scripting (XSS) filter built into modern web browsers. Explicitly setting X-XSS-Protection header to "0" will allow an attacker to perform XSS attack on your users..',
        href: "#",
      },
      {
        name: "Remediation",
        description:
          "The recommended configuration is to set this header to the following value, which will enable the XSS protection and instruct the browser to block the response in the event that a malicious script has been inserted from user input, instead of sanitizing. x-xss-protection: 1; mode=block.",
        href: "#",
      },
    ],
  },
];
