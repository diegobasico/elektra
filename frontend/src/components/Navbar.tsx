import React from "react";

function Navbar({
  activateComponent,
}: {
  activateComponent: React.Dispatch<React.SetStateAction<string>>;
}) {
  interface NavbarItemProps {
    id: string;
    component: () => void;
    text?: string;
  }

  const navbarItems: NavbarItemProps[] = [
    {
      id: "insert",
      component: () => activateComponent("Insert"),
      text: "Insert",
    },
    {
      id: "query",
      component: () => activateComponent("Query"),
      text: "Query",
    },
  ];

  function NavbarComponent({ data }: { data: NavbarItemProps[] }) {
    return (
      <>
        {data.map((item, index) => (
          <ul key={index}>
            <button
              className="mx-15 rounded-md bg-blue-900 px-2 py-0.5"
              onClick={item.component}
            >
              {item.text}
            </button>
          </ul>
        ))}
      </>
    );
  }

  return (
    <div className="flex h-12 items-center justify-center bg-blue-950">
      <NavbarComponent data={navbarItems} />
    </div>
  );
}

export default Navbar;
