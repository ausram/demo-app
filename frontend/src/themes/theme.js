import { createTheme } from '@mui/material/styles';

export const darkTheme = createTheme({
    primary: "#282c34",
    typography: {
        "fontFamily": `"Mulish", "Montserrat", "Calibri", "Roboto", "Helvetica", "Arial", sans-serif`,
    }
});

export const lightTheme = createTheme({
    primary: '#fff',
    typography: {
        "fontFamily": `"Mulish", "Montserrat", "Calibri", "Roboto", "Helvetica", "Arial", sans-serif`,
    }
});
