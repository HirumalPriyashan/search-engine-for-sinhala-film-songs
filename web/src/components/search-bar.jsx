import React from "react";
import { Formik } from "formik";
import { Box, Input, InputGroup, InputRightElement, FormControl } from "@chakra-ui/react";
import { SearchIcon } from "@chakra-ui/icons";

export const SearchBar = ({ placeholder = "", onSubmit = {} }) => {
    return (
        <Formik
            initialValues={{
                query: "",
            }}
            onSubmit={onSubmit}
        >
            {(props) => (
                <Box>
                    <FormControl>
                        <InputGroup>
                            <Input
                                id="query-input"
                                placeholder={placeholder}
                                name="query"
                                value={props.initialValues.query}
                                {...props.getFieldProps("query")}
                            />
                            <InputRightElement
                                onClick={props.submitForm}
                                children={<SearchIcon color="green.500" _hover={{ cursor: "pointer" }} />}
                            />
                        </InputGroup>
                    </FormControl>
                </Box>
            )}
        </Formik>
    );
};

export default SearchBar;
