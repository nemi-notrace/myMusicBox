import {
  ActionFunction,
  unstable_createFileUploadHandler,
  unstable_parseMultipartFormData,
  redirect
} from '@remix-run/node'
import fs from 'fs-extra'

export const action: ActionFunction = async ({ request }) => {
  fs.removeSync('/home/pi/2')

  const uploadHandler = unstable_createFileUploadHandler({
    maxFileSize: 15_000_000,
    directory: '/home/pi/2',
    file: ({ filename }) => filename
  })
  const formData = await unstable_parseMultipartFormData(request, uploadHandler)

  return redirect('/')
}
