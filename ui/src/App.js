import "./App.css";
import { Container, Typography, TextField } from "@mui/material";
import Steps from "./screens/Steps";
import AppBar from "@mui/material/AppBar";
import Button from "@mui/material/Button";
// import CameraIcon from "@mui/icons-material/PhotoCamera";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import CssBaseline from "@mui/material/CssBaseline";
import Grid from "@mui/material/Grid";
import Stack from "@mui/material/Stack";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Link from "@mui/material/Link";
import Avatar from "@mui/material/Avatar";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Paper from "@mui/material/Paper";
import { createTheme, ThemeProvider } from "@mui/material/styles";

function handleSubmit() {}
function Copyright() {
  return (
    <Typography variant="body2" color="text.secondary" align="center">
      {"Copyright © "}
      <Link color="inherit" href="https://mui.com/">
        Your Website
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}

const theme = createTheme();

function App() {
  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        {/* <AppBar position="relative" color="primary">
          <Toolbar>
            <Typography variant="h6" color="inherit" noWrap>
              streamline
            </Typography>
          </Toolbar>
        </AppBar> */}
        <Grid container component="main" sx={{ height: "100vh" }}>
          <Grid
            item
            xs={12}
            sm={8}
            md={7}
            component={Paper}
            elevation={6}
            square
            // style={{ backgroundColor: "grey" }}
          >
            <Steps />
          </Grid>
          <CssBaseline />
          <Grid
            item
            xs={false}
            sm={4}
            md={5}
            sx={{
              backgroundImage: "url(https://source.unsplash.com/random)",
              backgroundRepeat: "no-repeat",
              backgroundColor: (t) =>
                t.palette.mode === "light"
                  ? t.palette.grey[50]
                  : t.palette.grey[900],
              backgroundSize: "cover",
              backgroundPosition: "center",
            }}
          />
        </Grid>

        {/* Footer */}
      </ThemeProvider>
    </div>
  );
}

export default App;
