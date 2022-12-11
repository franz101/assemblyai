import * as React from "react";
import Box from "@mui/material/Box";
import Stepper from "@mui/material/Stepper";
import Step from "@mui/material/Step";
import StepLabel from "@mui/material/StepLabel";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import UsernameStep from "./ChannelStep";
import ChooseVideosStep from "./ChooseVideosStep";
import Paper from "@mui/material/Paper";
import Container from "@mui/material/Container";
import PlayCircleOutlineTwoToneIcon from "@mui/icons-material/PlayCircleOutlineTwoTone";
import { useState } from "react";
const steps = ["Connect Channel", "Select Videos", "Submitted"];

export default function Steps() {
  const [activeStep, setActiveStep] = useState(0);
  const [selectedVideos, setSelectedVideos] = useState([]);
  const [userPayload, setUserPayload] = useState({});

  const handleNext = () => {
    setActiveStep((prevActiveStep) => prevActiveStep + 1);
  };

  const onVideosSelected = (selectedVideos) => {
    setSelectedVideos(selectedVideos);
    finalize(selectedVideos);
    setActiveStep(2);
  };

  const finalize = (selectedVideos) => {
    fetch(`${process.env.REACT_APP_SERVER_HOST}/api/enqueue_videos`, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        video_ids: selectedVideos,
      }),
    })
      .then((r) => r.json())
      .then((response) => {
        console.log(response);
      })
      .catch(function (error) {
        console.log("Request failed", error);
        //setError(true);
      });
  };

  return (
    <Container component="main" sx={{ mb: 4 }}>
      <Box
        sx={{
          my: 2,
          mx: 2,
          display: "flex",
          flexDirection: "column",
          alignItems: "left",
        }}
      >
        <Typography
          component="h1"
          variant="h4"
          align="left"
          style={{ fontFamily: "HelveticaNeue-Light", letterSpacing: 2 }}
        >
          <PlayCircleOutlineTwoToneIcon sx={{ mr: 1, mb: -0.25 }} />
          <b>stream</b>line
        </Typography>
        <div>{/* <img src="./logo.png" height="80px" /> */}</div>

        {
          <>
            <Stepper activeStep={activeStep} sx={{ pt: 4 }}>
              {steps.map((label, index) => {
                const stepProps = {};
                const labelProps = {};
                return (
                  <Step key={label} {...stepProps}>
                    <StepLabel {...labelProps}>{label}</StepLabel>
                  </Step>
                );
              })}
            </Stepper>
          </>
        }

        <>
          <Box
            sx={{
              my: 2,

              display: "flex",
              flexDirection: "column",
              alignItems: "center",
            }}
          >
            <Box sx={{ flex: "1 1 auto" }} />
            {activeStep === 0 && (
              <UsernameStep
                onComplete={(userPayload) => {
                  setUserPayload(userPayload);
                  handleNext();
                }}
              />
            )}
            {activeStep === 1 && (
              <ChooseVideosStep
                onVideosSelected={onVideosSelected}
                data={userPayload}
              />
            )}

            {activeStep === 2 && (
              <div>
                <Typography variant="h5" gutterBottom component="div">
                  Thank you for your submission!
                </Typography>
                <Box mt={3}>
                  The following video IDs will be submitted:
                  {selectedVideos.map((videoId) => {
                    return <div key={videoId}>{videoId}</div>;
                  })}
                </Box>
              </div>
            )}
          </Box>
        </>
      </Box>
      {/* </Paper> */}
    </Container>
  );
}
