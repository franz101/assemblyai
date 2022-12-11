import * as React from "react";
import { DataGrid } from "@mui/x-data-grid";

const columns = [
  {
    field: "thumbnail",
    headerName: "",
    width: 200,
    renderCell: (params) => {
      return (
        <div>
          <img src={params.row.thumbnail} alt="" width="100%" />
        </div>
      );
    },
  },
  { field: "title", headerName: "Title", width: 410 },
  {
    field: "date",
    headerName: "Date",
    width: 200,
    renderCell: (params) => {
      return new Date(params.row.date).toLocaleDateString();
    },
  },
];

export default function VideoChooser({ setSelectedVideos, videos }) {
  return (
    <div style={{ height: 800, width: "100%" }}>
      <DataGrid
        fullWidth
        rowHeight={200}
        rows={videos}
        columns={columns}
        pageSize={10}
        rowsPerPageOptions={[50]}
        onSelectionModelChange={(ids) => {
          // const selectedIDs =
          // const selectedRowData = rows.filter((row) =>
          //   selectedIDs.has(row.id.toString());
          // );
          setSelectedVideos(ids);
          console.log(ids);
        }}
        checkboxSelection
      />
    </div>
  );
}
