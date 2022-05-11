import { Box, Heading, VStack, Text, Center } from '@chakra-ui/react'
import { Form } from '@remix-run/react'
import Dropzone from '~/components/dropzone'

export default function Index () {
  return (
    <VStack>
      <Box>
        <Heading textAlign={'center'}>myMusicbox Upload</Heading>

        <Text textAlign={'center'}>
          <b> Load up your .mp3 files to the Button you like.</b>
          <br />
          <small> Other files my work but can also crash the system.</small>
        </Text>
      </Box>

      <Form method='post' action='/dropOne' encType='multipart/form-data'>
        <Dropzone identifier='one' bgColor='red.50'></Dropzone>
      </Form>

      <Form method='post' action='/dropTwo' encType='multipart/form-data'>
        <Dropzone identifier='two' bgColor='green.50'></Dropzone>
      </Form>

      <Form method='post' action='/dropThree' encType='multipart/form-data'>
        <Dropzone identifier='three' bgColor='blue.50'></Dropzone>
      </Form>
      <Text>All uploaded files will be deleted if you upload new files.</Text>
    </VStack>
  )
}
