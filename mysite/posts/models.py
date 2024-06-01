from django.db import models

# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    WARRANTY_CHOICES = [
        ('1สัปดาห์','1สัปดาห์'),
        ('2สัปดาห์','2สัปดาห์'),
        ('3สัปดาห์','3สัปดาห์'),
        ('1เดือน','1เดือน'),
        ('2เดือน','2เดือน'),
        ('3เดือน','3เดือน'),
        ('4เดือน','4เดือน'),
        ('5เดือน','5เดือน'),
        ('6เดือน','6เดือน'),
        ('7เดือน','7เดือน'),
        ('8เดือน','8เดือน'),
        ('9เดือน','9เดือน'),
        ('10เดือน','10เดือน'),
        ('11เดือน','11เดือน'),
        ('1ปี','1ปี'),
    ]
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    name = models.CharField(max_length=300,null=True)
    description = models.TextField(null=True)
    price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    image1 = models.ImageField(upload_to='static/product_images/',blank=True)
    image2 = models.ImageField(upload_to='static/product_images/', blank=True)
    image3 = models.ImageField(upload_to='static/product_images/', blank=True)
    warranty = models.CharField(max_length=8, choices=WARRANTY_CHOICES,null=True)
    has_detail = models.BooleanField(default=False)
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}"

class Computer(models.Model):
    BRAND_CHOICES = [
        ('HP', 'HP'),
        ('DELL', 'DELL'),
        ('ASUS', 'ASUS'),
        ('ACER', 'ACER'),
        ('LENOVO', 'LENOVO'),
        ('MSI', 'MSI'),
        ('APPLE', 'APPLE'),
    ]
    
    SYSTEM_CHOICES = [
        ('WINDOW', 'WINDOW'),
        ('IOS', 'IOS'),
    ]

    RAM_CHOICES = [
        ('2', '2'),
        ('4', '4'),
        ('6', '6'),
        ('8', '8'),
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('16', '16'),
        ('18', '18'),
        ('20', '20'),
    ]

    ROM_CHOICES = [
        ('128GB HHD', '128GB HHD'),
        ('256GB HHD', '256GB HHD'),
        ('512GB HHD', '512GB HHD'),
        ('1TB HHD', '1TB HHD'),
        ('2TB HHD', '2TB HHD'),
        ('3TB HHD', '3TB HHD'),
        ('4TB HHD', '4TB HHD'),
        ('5TB HHD', '5TB HHD'),
        ('128GB SSD', '128GB SSD'),
        ('256GB SSD', '256GB SSD'),
        ('512GB SSD', '512GB SSD'),
        ('1TB SSD', '1TB SSD'),
        ('2TB SSD', '2TB SSD'),
        ('3TB SSD', '3TB SSD'),
        ('4TB SSD', '4TB SSD'),
        ('5TB SSD', '5TB SSD'),
    ]

    CPU_BAND_CHOICES = [
        ('INTEL', 'INTEL'),
        ('AMD', 'AMD'),
        ('APPLE', 'APPLE'),
    ]

    CPU_GEN_CHOICES = [
        ('CELERON', 'CELERON'),
        ('PENTIUM', 'PENTIUM'),
        ('Core I3', 'Core I3'),
        ('Core I5', 'Core I5'),
        ('Core I7', 'Core I7'),
        ('Core I9', 'Core I9'),
        ('RYZEN 3', 'RYZEN 3'),
        ('RYZEN 5', 'RYZEN 5'),
        ('RYZEN 7', 'RYZEN 7'),
        ('RYZEN 9', 'RYZEN 9'),
        ('M1', 'M1'),
        ('M1 Pro', 'M1 Pro'),
        ('M1 Max', 'M1 Max'),
        ('M2', 'M2'),
        ('M2 Pro', 'M2 Pro'),
        ('M2 Max', 'M2 Max'),
        ('M3', 'M3'),
        ('M3 Pro', 'M3 Pro'),
        ('M3 Max', 'M3 Max'),
    ]

    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='computer')
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    accessorise = models.CharField(max_length=300)
    mainboard = models.CharField(max_length=300, null=True)
    powersupply = models.CharField(max_length=300, null=True)
    cpu_band = models.CharField(max_length=50, choices=CPU_BAND_CHOICES)
    cpu_gen = models.CharField(max_length=50, choices=CPU_GEN_CHOICES)
    cpu_series = models.CharField(max_length=300, null=True)
    ram = models.CharField(max_length=50, choices=RAM_CHOICES)
    rom = models.CharField(max_length=50, choices=ROM_CHOICES)
    gpu = models.CharField(max_length=100)
    system = models.CharField(max_length=50, choices=SYSTEM_CHOICES)

    def __str__(self):
        if self.product:
            return f"{self.brand} {self.product.name} "
        else:
            return "No product"


class Notebook(models.Model):
    BRAND_CHOICES = [
        ('HP', 'HP'),
        ('DELL', 'DELL'),
        ('ASUS', 'ASUS'),
        ('ACER', 'ACER'),
        ('LENOVO', 'LENOVO'),
        ('MSI', 'MSI'),
        ('APPLE', 'APPLE'),
    ]
    
    SYSTEM_CHOICES = [
        ('WINDOW', 'WINDOW'),
        ('IOS', 'IOS'),
    ]

    RAM_CHOICES = [
        ('2', '2'),
        ('4', '4'),
        ('6', '6'),
        ('8', '8'),
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('16', '16'),
        ('18', '18'),
        ('20', '20'),
    ]

    ROM_CHOICES = [
        ('128GB HHD', '128GB HHD'),
        ('256GB HHD', '256GB HHD'),
        ('512GB HHD', '512GB HHD'),
        ('1TB HHD', '1TB HHD'),
        ('2TB HHD', '2TB HHD'),
        ('3TB HHD', '3TB HHD'),
        ('4TB HHD', '4TB HHD'),
        ('5TB HHD', '5TB HHD'),
        ('128GB SSD', '128GB SSD'),
        ('256GB SSD', '256GB SSD'),
        ('512GB SSD', '512GB SSD'),
        ('1TB SSD', '1TB SSD'),
        ('2TB SSD', '2TB SSD'),
        ('3TB SSD', '3TB SSD'),
        ('4TB SSD', '4TB SSD'),
        ('5TB SSD', '5TB SSD'),
    ]

    CPU_BAND_CHOICES = [
        ('INTEL', 'INTEL'),
        ('AMD', 'AMD'),
        ('APPLE', 'APPLE'),
    ]

    CPU_GEN_CHOICES = [
        ('CELERON', 'CELERON'),
        ('PENTIUM', 'PENTIUM'),
        ('Core I3', 'Core I3'),
        ('Core I5', 'Core I5'),
        ('Core I7', 'Core I7'),
        ('Core I9', 'Core I9'),
        ('RYZEN 3', 'RYZEN 3'),
        ('RYZEN 5', 'RYZEN 5'),
        ('RYZEN 7', 'RYZEN 7'),
        ('RYZEN 9', 'RYZEN 9'),
        ('M1', 'M1'),
        ('M1 Pro', 'M1 Pro'),
        ('M1 Max', 'M1 Max'),
        ('M2', 'M2'),
        ('M2 Pro', 'M2 Pro'),
        ('M2 Max', 'M2 Max'),
        ('M3', 'M3'),
        ('M3 Pro', 'M3 Pro'),
        ('M3 Max', 'M3 Max'),
    ]

    DISPLAYS = [
        ('13.3', '13.3'),
        ('14.0', '14.0'),
        ('15.6', '15.6'),
        ('16.0', '16.0'),
        ('17.3', '17.3'),
    ]

    CAMERA = [
        ('ไม่มี', 'ไม่มี'),
        ('มี', 'มี'),
    ]
   
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='notebook')
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    accessorise = models.CharField(max_length=300)
    cpu_band = models.CharField(max_length=50, choices=CPU_BAND_CHOICES)
    cpu_gen = models.CharField(max_length=50, choices=CPU_GEN_CHOICES)
    cpu_series = models.CharField(max_length=300, null=True)
    display = models.CharField(max_length=50, choices=DISPLAYS , null=True)
    camera = models.CharField(max_length=50, choices=CAMERA , null=True)
    ram = models.CharField(max_length=50, choices=RAM_CHOICES)
    rom = models.CharField(max_length=50, choices=ROM_CHOICES)
    gpu = models.CharField(max_length=100)
    system = models.CharField(max_length=50, choices=SYSTEM_CHOICES)

    def __str__(self):
        if self.product:
            return f"{self.product.name}"
        else:
            return "No product"

    
class Monitor(models.Model):
    BRAND_CHOICES = [
        ('HP', 'HP'),
        ('DELL', 'DELL'),
        ('ASUS', 'ASUS'),
        ('ACER', 'ACER'),
        ('LENOVO', 'LENOVO'),
        ('MSI', 'MSI'),
        ('VIEWSONIC', 'VIEWSONIC'),
        ('ZOWIE', 'ZOWIE'),
        ('APPLE', 'APPLE'),
    ]

    SIZE_CHOICES = [
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('21', '21'),
        ('23', '23'),
        ('24', '24'),
        ('27', '27'),
        ('30', '30'),
        ('32', '32'),
        ('34', '34'),
    ]

    PANEL_CHOICES = [
        ('TN', 'TN'),
        ('VA', 'VA'),
        ('IPS', 'IPS'),
        ('OLED', 'OLED'),
        ('QLED', 'QLED'),
    ]

    REFRESH_RATE_CHOICES = [
        ('60Hz', '60Hz'),
        ('75Hz', '75Hz'),
        ('100Hz', '100Hz'),
        ('144Hz', '144Hz'),
        ('240Hz', '240Hz'),
        ('360Hz', '360Hz'),
    ]

    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='monitor')
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    panel = models.CharField(max_length=50, choices=PANEL_CHOICES)
    refresh_rate = models.CharField(max_length=50, choices=REFRESH_RATE_CHOICES)

    def __str__(self):
        if self.product:
            return f"{self.product.name}"
        else:
            return "No product"

    
class MouseKeyboard(models.Model):
    BRAND_CHOICES = [
        ('Logitech', 'Logitech'),
        ('Razer', 'Razer'),
        ('SteelSeries', 'SteelSeries'),
        ('Corsair', 'Corsair'),
        ('ASUS', 'ASUS'),
        ('HP', 'HP'),
        ('Dell', 'Dell'),
        ('Microsoft', 'Microsoft'),
        ('Cooler Master', 'Cooler Master'),
        ('HyperX', 'HyperX'),
        ('Zowie', 'Zowie'),
    ]

    DPI_CHOICES = [
        ('1000','1000'),
        ('2000','2000'),
        ('3000','3000'),
        ('4000','4000'),
        ('5000','5000'),
        ('6000','6000'),
        ('7000','7000'),
        ('8000','8000'),
        ('9000','9000'),
        ('10000','10000'),
    ]

    CONNECT_CHOICES = [
        ('USB', 'USB'),
        ('Wireless', 'Wireless'),
        ('Bluetooth', 'Bluetooth'),
        ('Wireless Receiver', 'Wireless Receiver'),
        ('Thunderbolt', 'Thunderbolt'),
        ('Ethernet', 'Ethernet'),
    ]

    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='mousekeyboard')
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    dpi = models.CharField(max_length=50, choices=DPI_CHOICES ,blank=True)
    connect = models.CharField(max_length=50, choices=CONNECT_CHOICES)

    def __str__(self):
        if self.product:
            return f"{self.product.name}"
        else:
            return "No product"


class HeadphoneSpeakers(models.Model):
    BRAND_CHOICES = [
        ('Sennheiser', 'Sennheiser'),
        ('Sony', 'Sony'),
        ('Audio-Technica', 'Audio-Technica'),
        ('Bose', 'Bose'),
        ('JBL', 'JBL'),
        ('AKG', 'AKG'),
        ('Beyerdynamic', 'Beyerdynamic'),
        ('Beats by Dre', 'Beats by Dre'),
        ('SteelSeries', 'SteelSeries'),
        ('Skullcandy', 'Skullcandy'),
        ('Harman Kardon', 'Harman Kardon'),
        ('Marshall', 'Marshall'),
        ('Nubwo', 'Nubwo'),
        ('Sonos', 'Sonos'),
        ('Bang & Olufsen', 'Bang & Olufsen'),
        ('Logitech', 'Logitech'),
        ('Edifier', 'Edifier'),
        ('อื่นๆ', 'อื่นๆ'),
    ]


    CONNECT_CHOICES = [
        ('USB', 'USB'),
        ('Wireless', 'Wireless'),
        ('Bluetooth', 'Bluetooth'),
        ('Wireless Receiver', 'Wireless Receiver'),
        ('Thunderbolt', 'Thunderbolt'),
        ('Ethernet', 'Ethernet'),
    ]

    SIZE_CHOICES = [
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Medium', 'Medium'),
    ]


    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='headphonespeaker')
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    connect = models.CharField(max_length=50, choices=CONNECT_CHOICES)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)

    def __str__(self):
        if self.product:
            return f"{self.product.name}"
        else:
            return "No product"


class Printers(models.Model):
    BRAND_CHOICES = [
        ('HP', 'HP'),
        ('Canon', 'Canon'),
        ('Epson', 'Epson'),
        ('Brother', 'Brother'),
        ('Samsung', 'Samsung'),
        ('Xerox', 'Xerox'),
        ('Kyocera', 'Kyocera'),
    ]

    COLOR_CHOICES = [
        ('Color', 'สี'),
        ('Monochrome', 'ขาว-ดำ'),
        ('Both', 'สีและขาว-ดำ'),
    ]

    INK_TYPE_CHOICES = [
        ('Inkjet', 'หมึกแทงค์ (Inkjet)'),
        ('Laser', 'เลเซอร์ (Laser)'),
        ('Dot Matrix', 'ดอทเมทริกซ์ (Dot Matrix)'),
        ('Thermal', 'เทอร์มัล (Thermal)'),
        ('Solid Ink', 'หมึกแข็ง (Solid Ink)'),
        ('Dye Sublimation', 'ไดซับลิเมชัน (Dye Sublimation)'),
    ]

    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='printer')
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    type_of_ink = models.CharField(max_length=50, choices=INK_TYPE_CHOICES)

    def __str__(self):
        if self.product:
            return f"{self.product.name}"
        else:
            return "No product"

    
class SDCards_USBs(models.Model):
    CAPACITY_CHOICES = [
        ('4GB', '4GB'),
        ('8GB', '8GB'),
        ('16GB', '16GB'),
        ('32GB', '32GB'),
        ('64GB', '64GB'),
        ('128GB', '128GB'),
        ('256GB', '256GB'),
    ]

    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='sdcards_usb')
    brand = models.CharField(max_length=100)
    capacity = models.CharField(max_length=10, choices=CAPACITY_CHOICES)
    speed = models.CharField(max_length=50)

    def __str__(self):
        if self.product:
            return f"{self.product.name}"
        else:
            return "No product"

    
class ConnectivityDevices(models.Model):
    TYPE_CHOICES = [
        ('Ethernet', 'สายแลน (Ethernet Cable)'),
        ('USB', 'สาย USB (USB Cable)'),
        ('HDMI', 'สาย HDMI (HDMI Cable)'),
        ('DVI', 'สาย DVI (DVI Cable)'),
        ('VGA', 'สาย VGA (VGA Cable)'),
        ('DisplayPort', 'สาย DisplayPort (DisplayPort Cable)'),
        ('Audio', 'สายออดิโอ (Audio Cable)'),
        ('Power', 'สายไฟ (Power Cable)'),
    ]

    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='connectivitydevice')
    brand = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        if self.product:
            return f"{self.product.name}"
        else:
            return "No product"
