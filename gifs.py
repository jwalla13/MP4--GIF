import imageio
import os


entry=input("Please enter the name of the file you would like to convert, including the file type: ")
clip = os.path.abspath(entry)


def gifConvert(inputPath, targetFormat):
    global entry
    outputPath = os.path.splitext(inputPath)[0] + targetFormat

    print(f'converting {entry} \n to {targetFormat}')

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(outputPath, fps=fps)

    for frames in reader:
        writer.append_data(frames)
    print('Done!')
    writer.close()

gifConvert(clip, '.gif')

