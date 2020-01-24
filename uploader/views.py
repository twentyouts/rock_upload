from aiohttp import web
import os

async def upload(request):

    text = """
        <!doctype html>
        <html>
        <head>
        </head>
        <body>

        </body>
        </html>


        <!doctype html>
        <html lang="en">
        <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

            <!-- Bootstrap CSS -->
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
        </head>
        <body>

            <form action="/upload" method="post" enctype="multipart/form-data">
                <div>
                <label for="file">Choose file to upload</label>
                <input type="file" id="file" name="file" multiple>
                </div>
                <div>
                <button>Submit</button>
                </div>
            </form>
            <!-- Optional JavaScript -->
            <!-- jQuery first, then Popper.js, then Bootstrap JS -->
            <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

        
        </body>
        </html>
    """
    return web.Response(text=text, content_type='text/html')

# async def make_upload(request):
#     post_request = await request.multipart()


#     data = post_request['file']
#     file_name = data.filename
#     file_data = data.file
#     content = file_data.read()

#     return web.Response(text = 'Done')


async def make_upload(request):

    reader = await request.multipart()

    # /!\ Don't forget to validate your inputs /!\

    # reader.next() will `yield` the fields of your form

    # field = await reader.next()
    # # print(field.name)
    # # assert field.name == 'file'

    # name = await field.read(decode=True)
    curent_dir = os.getcwd() + '/uploads/'


    field = await reader.next()
    assert field.name == 'file'
    filename = field.filename
    # You cannot rely on Content-Length if transfer is chunked.
    size = 0
    with open(os.path.join(curent_dir, filename), 'wb') as f:
        while True:
            chunk = await field.read_chunk()  # 8192 bytes by default.
            if not chunk:
                break
            size += len(chunk)
            f.write(chunk)

    return web.Response(text='{} sized of {} successfully stored'
                             ''.format(filename, size))


async def hello(request):
    return web.Response(text='Hello from manin!')    
