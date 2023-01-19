import * as React from "react";
import {
    Accordion,
    AccordionItem,
    AccordionButton,
    AccordionPanel,
    AccordionIcon,
    Box,
    Card,
    CardBody,
    Text,
    Highlight,
    Divider,
} from "@chakra-ui/react";

const InfoComponent = ({ header, sinhala, english, other }) => {
    return sinhala ? (
        <Box as="span" flex="1" textAlign="left">
            <Text as="b">{header}</Text>
            <Text as="i" p={2}>
                {sinhala}
            </Text>
            <Text as="i" fontSize="xs" color="gray.600" pr={2}>
                {english}
            </Text>
            {other && (
                <Text as="i" color="gray.800">
                    {other}
                </Text>
            )}
        </Box>
    ) : (
        <Box />
    );
};
// https://github.com/gatsbyjs/gatsby-starter-shopify
export const SongCard = ({ songInfo }) => {
    return songInfo.metaphors.map((metaphor, index) => (
        <Card
            direction={{ base: "column", sm: "row" }}
            overflow="hidden"
            variant="elevated"
            border="1px"
            borderColor="gray.200"
            boxShadow="xl"
            m={2}
            rounded="md"
            key={songInfo.film_no + index}
        >
            <CardBody>
                {/* Metaphor info */}
                <Box>
                    {/* <Text as="b">Line :</Text> */}
                    <Highlight query={metaphor.target} styles={{ px: "1", py: "1", bg: "orange.100" }}>
                        {metaphor.line}
                    </Highlight>
                </Box>
                <Divider size="lg" />
                <Box>
                    <Text as="b">Target :</Text>
                    <Text as="i">{metaphor.target}</Text>
                </Box>

                <Box>
                    <Text as="b">Source :</Text>
                    <Text as="i">{metaphor.source}</Text>
                </Box>

                <Box>
                    <Text as="b">Meaning :</Text>
                    <Text as="i">{metaphor.meaning}</Text>
                </Box>

                <Box>
                    <Text as="b">Domain :</Text>
                    <Text as="i">{metaphor.domain}</Text>
                </Box>

                {/* Song Information */}
                <Accordion allowMultiple pt={2} ml="-4">
                    <AccordionItem>
                        <AccordionButton>
                            <InfoComponent
                                header="Song title :"
                                sinhala={songInfo.title}
                                english={songInfo.title_english}
                            />
                        </AccordionButton>
                        <AccordionPanel pb={4} pl="12">
                            <InfoComponent
                                header="Artist : "
                                sinhala={songInfo.artist.join(", ")}
                                english={songInfo.artist_english.join(", ")}
                            />
                            <InfoComponent
                                header="Lyrics by :"
                                sinhala={songInfo.lyrics_by}
                                english={songInfo.lyrics_by_english}
                            />
                            <InfoComponent
                                header="Music by :"
                                sinhala={songInfo.music_by}
                                english={songInfo.music_by_english}
                            />
                            <Accordion allowToggle>
                                <AccordionItem>
                                    <AccordionButton pl={-2}>
                                        <AccordionIcon />
                                        <Box as="span" flex="1" textAlign="left">
                                            <Text as="b">Lyrics</Text>
                                        </Box>
                                    </AccordionButton>
                                    <AccordionPanel pb={4}>{songInfo.lyrics}</AccordionPanel>
                                </AccordionItem>
                            </Accordion>
                        </AccordionPanel>
                    </AccordionItem>

                    <AccordionItem>
                        <AccordionButton>
                            <InfoComponent
                                header="Film :"
                                sinhala={songInfo.film}
                                english={songInfo.film_english}
                                other={songInfo.release_date}
                            />
                        </AccordionButton>
                        <AccordionPanel pb={4} pl="12">
                            <InfoComponent
                                header="Film genres :"
                                sinhala={songInfo.film_genres.join(", ")}
                                english={songInfo.film_genres_english.join(", ")}
                            />
                            <InfoComponent
                                header="Main Actors :"
                                sinhala={songInfo.main_actors.join(", ")}
                                english={songInfo.main_actors_english.join(", ")}
                            />
                            <InfoComponent
                                header="Main Actresses :"
                                sinhala={songInfo.main_actresses.join(", ")}
                                english={songInfo.main_actresses_english.join(", ")}
                            />
                            <InfoComponent
                                header="Directors :"
                                sinhala={songInfo.directors.join(", ")}
                                english={songInfo.directors_english.join(", ")}
                            />
                            <InfoComponent
                                header="Producers :"
                                sinhala={songInfo.producers.join(", ")}
                                english={songInfo.producers_english.join(", ")}
                            />
                        </AccordionPanel>
                    </AccordionItem>
                </Accordion>
            </CardBody>
        </Card>
    ));
};
