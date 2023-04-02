export const demouser = {
  name: "noname",
  email: "tom@example.com",
  imageUrl:
    "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
};
export const navigation = [
  { name: "Report", href: "/dashboard", current: false },
  { name: "History", href: "/history", current: true },
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
  { name: "Features", href: "#Features" },
  { name: "Documentation", href: "/Frontend/src/pages/Documentation.jsx" },
  { name: "Community", href: "#Community" },
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

export const auditHistoryData = {
  title: "Audit History",
  data: [
    {
      id: 1,
      title: "https://example.com",
      type: "High",
      category: "6th March 2023",
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
      title: "https://example.com",
      type: "High",
      category: "5th March 2023",
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
  ],
};

export const people = [
  {
    number: 12345,
    website: "https://example.com",
    status: "Completed",
    createdAt: "06-03-2023",
    updatedAt: "06-03-2023",
  },
  {
    number: 23456,
    website: "https://example.com",
    status: "Pending",
    createdAt: "05-03-2023",
    updatedAt: "06-03-2023",
  },
  {
    number: 23456,
    website: "https://example.com",
    status: "Stopped",
    createdAt: "01-03-2023",
    updatedAt: "03-03-2023",
  },
  // More people...
];

export const scannerData = {
  "Scan Results": {
    alerts: [
      {
        sourceid: "3",
        other: "",
        method: "GET",
        evidence: "",
        pluginId: "10020",
        cweid: "1021",
        confidence: "Medium",
        wascid: "15",
        description:
          "The response does not include either Content-Security-Policy with 'frame-ancestors' directive or X-Frame-Options to protect against 'ClickJacking' attacks.",
        messageId: "28",
        inputVector: "",
        url: "https://public-firing-range.appspot.com/address/index.html",
        tags: {
          OWASP_2021_A05:
            "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/",
          "WSTG-v42-CLNT-09":
            "https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client-side_Testing/09-Testing_for_Clickjacking",
          OWASP_2017_A06:
            "https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html",
        },
        reference:
          "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options",
        solution:
          "Modern Web browsers support the Content-Security-Policy and X-Frame-Options HTTP headers. Ensure one of them is set on all web pages returned by your site/app.\nIf you expect the page to be framed only by pages on your server (e.g. it's part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never expect the page to be framed, you should use DENY. Alternatively consider implementing Content Security Policy's \"frame-ancestors\" directive.",
        alert: "Missing Anti-clickjacking Header",
        param: "X-Frame-Options",
        attack: "",
        name: "Missing Anti-clickjacking Header",
        risk: "Medium",
        id: "0",
        alertRef: "10020-1",
      },
    ],
  },
};
