import * as React from 'react';
import { DataGrid } from '@mui/x-data-grid';

const columns = [
  { field: 'thumbnail', headerName: 'Thumbnail', width: 320, renderCell: (params)=> {
    return (
      <div>
        <img src={params.row.thumbnail} alt='' />
      </div>
    )
  }},
  { field: 'title', headerName: 'Title', width: 430 },
  { field: 'date', headerName: 'Date', width: 200 }
];

export default function VideoChooser(props) {
  return (
    <div style={{ height: 800, width: '100%' }}>
      <DataGrid
        rowHeight={200}
        rows={props.videos}
        columns={columns}
        pageSize={5}
        rowsPerPageOptions={[50]}
        onSelectionModelChange={(ids) => {
            // const selectedIDs = 
            // const selectedRowData = rows.filter((row) =>
            //   selectedIDs.has(row.id.toString());
            // );
            props.setSelectedVideos(ids);
            console.log(ids);
          }}
        checkboxSelection
      />
    </div>
  );
}