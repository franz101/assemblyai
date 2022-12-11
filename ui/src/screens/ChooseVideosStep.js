import { useEffect, useState } from "react";
import { Box, Container, Button } from "@mui/material";
import VideoChooser from "../components/VideoChooser";

const ChooseVideosStep = (props) => {
  const [videos, setVideos] = useState([]);
  const [selectedVideos, setSelectedVideos] = useState([]);

  useEffect(() => {
    fetch(
      `${process.env.REACT_APP_SERVER_HOST}/api/fetch_channel_videos/${props.data.channel_id}`
    )
      .then((r) => r.json())
      .then((response) => {
        const videoRows = response.items.filter(
          (row) => row.id.kind === "youtube#video"
        );
        const rows = videoRows.map((row) => {
          return {
            id: row.id.videoId,
            thumbnail: row.snippet.thumbnails.medium.url,
            title: row.snippet.title,
            date: row.snippet.publishTime,
          };
        });

        setVideos(rows);
      })
      .catch(function (error) {
        console.log("Request failed", error);
      });
    // eslint-disable-next-line
  }, []);

  const submitSelected = () => {
    props.onVideosSelected(selectedVideos, videos);
  };

  return (
    <div style={{ width: "100%", paddingTop: 10 }}>
      <VideoChooser videos={videos} setSelectedVideos={setSelectedVideos} />
      <Box mt={3}>
        {/* <Button variant="text">Back</Button> */}
        <Button onClick={submitSelected} fullWidth variant="contained">
          Submit
        </Button>
      </Box>
    </div>
  );
};

export default ChooseVideosStep;
