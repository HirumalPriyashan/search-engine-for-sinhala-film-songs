import * as React from "react";
import { ChakraProvider } from "@chakra-ui/react";

import Main from "./main";

const App = () => {
    return (
        <ChakraProvider>
            <Main />
        </ChakraProvider>
    );
};

export default App;

export const Head = () => <title>Sinhala Movie Songs</title>;
