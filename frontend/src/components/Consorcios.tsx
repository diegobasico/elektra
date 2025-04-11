import { useRef, useEffect, useState } from "react";
import axios from "axios";

import { registerAllModules } from "handsontable/registry";
import { HotTable, HotTableRef } from "@handsontable/react-wrapper";

registerAllModules();

function Consorcios() {
  // const [tableData, setTableData] = useState([[null]]);
  const [consorciosDropdown, setConsorciosDropdown] = useState([""]);
  const [empresasDropdown, setEmpresasDropdown] = useState([""]);
  const hotRef = useRef<HotTableRef>(null);

  type Empresa = {
    id: number;
    nombre: string;
    ruc: number;
  };

  type Consorcio = {
    id: number;
    nombre: string;
  };

  useEffect(() => {
    const fetchDropdowns = async () => {
      try {
        const [consorciosResponse, empresasResponse] = await Promise.all([
          axios.get("http://localhost:8000/consorcios"),
          axios.get("http://localhost:8000/empresas"),
        ]);

        const empresas = empresasResponse.data;
        const consorcios = consorciosResponse.data;

        const extractNames = (items: Empresa[] | Consorcio[]) => {
          return items.map((item) => item.nombre);
        };

        setEmpresasDropdown(extractNames(empresas));
        setConsorciosDropdown(extractNames(consorcios));
      } catch (error) {
        console.error("Error fetching dropdowns:", error);
      }
    };

    fetchDropdowns();
  }, []);

  async function sendTableData() {
    const hot = hotRef.current?.hotInstance;

    try {
      await axios.post(
        "http://127.0.0.1:8000/consorcios_empresas_m2m",
        { table: hot?.getData() },
        {
          headers: { "Content-Type": "application/json" },
        },
      );
    } catch (error) {
      console.error("Error:", error);
    }
  }

  return (
    <div className="flex h-full w-full flex-col">
      <div className="p-4">
        <span className="text-3xl">Let's Insert!</span>
        <button className="border" onClick={sendTableData}>
          send data
        </button>
      </div>
      {/* Hands On Table Component */}
      <div className="ht-theme-main overflow-y-auto">
        <HotTable
          ref={hotRef}
          columns={[
            {
              type: "dropdown", // Consorcio
              source: consorciosDropdown,
            },
            {
              type: "dropdown", // Empresa
              source: empresasDropdown,
            },
            {
              type: "numeric", // Participación
              numericFormat: {
                pattern: "0.00%",
              },
            },
          ]}
          rowHeaders={false}
          colHeaders={["Consorcio", "Empresa", "Participación"]}
          autoWrapRow={true}
          autoWrapCol={true}
          licenseKey="non-commercial-and-evaluation"
          minSpareRows={1}
          stretchH="all"
          width="100%"
          height="auto"
          contextMenu={{
            items: {
              copy: {},
              cut: {},
              "---------": {},
              row_above: {},
              row_below: {},
              remove_row: {},
            },
          }}
          hiddenColumns={{
            columns: [],
            indicators: true,
            copyPasteEnabled: false,
          }}
          manualColumnMove={false}
          manualColumnFreeze={true}
          manualColumnResize={true}
          filters={false}
          hiddenRows={{
            rows: [],
            indicators: true,
            copyPasteEnabled: false,
          }}
          manualRowMove={true}
          manualRowResize={true}
          columnSorting={true}
          mergeCells={true}
        />
      </div>
    </div>
  );
}

export default Consorcios;
