import {
  FormControl,
  FormHelperText,
  Input,
  Box,
  Button,
  InputGroup,
  HStack,
  VStack
} from '@chakra-ui/react'
import { ChangeEvent, useEffect, useRef, useState } from 'react'
import { useTransition } from '@remix-run/react'

function fileListToArray (fileList: any) {
  const files = []
  for (let i = 0; i < fileList.length; i++) {
    files.push(fileList.item(i))
  }
  return files
}

export default function Dropzone (props: any) {
  const [input, setInput] = useState<any>([])
  let inputRef = useRef<any>()
  function handleInputChange (e: ChangeEvent<HTMLInputElement>) {
    setInput(fileListToArray(e.target.files))
  }
  const transition = useTransition()
  const busy = transition.submission
  const isAdding =
    transition.state === 'submitting' &&
    transition.submission.formData.get('_action') === props.identifier
  useEffect(() => {
    if (!isAdding) {
      setInput((inputRef.current.fileList = []))
      inputRef.current.value = ''
    }
  }, [isAdding])

  return (
    <Box boxShadow='md' p='6' rounded='md' bg={props.bgColor}>
      <HStack>
        <FormControl isRequired padding='10px'>
          <Box>
            <InputGroup>
              <Input
                ref={inputRef}
                placeholder='upload your music'
                id={props.identifier}
                name={props.identifier}
                type={'file'}
                readOnly
                onChange={handleInputChange}
                accept='.mp3,audio/'
                multiple
                opacity={'1'}
              ></Input>
            </InputGroup>
          </Box>

          <VStack justify='center' textAlign={'center'}>
            <Box>
              <FormHelperText>
                you can use drag and drop or click to select files for upload
              </FormHelperText>
            </Box>

            <Box>
              <Button
                name='_action'
                value={props.identifier}
                _hover={{
                  background: 'white',
                  color: 'blue.500'
                }}
                type='submit'
              >
                {isAdding ? 'uploading...' : 'submit'}
              </Button>
            </Box>
          </VStack>
        </FormControl>
      </HStack>
    </Box>
  )
}
