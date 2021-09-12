import sys
from io import BytesIO
from django.conf import settings
import os
import subprocess
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


class CompressImageBeforeUpload:
    def save(self, *args, **kwargs):
        im = Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((100, 100))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=90)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)

        return super().save(*args, **kwargs)
