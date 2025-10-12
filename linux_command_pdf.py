from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont

# Define commands
linux_commands = {
    "System Information": [
        ("uname -a", "Show all system information", "uname -a"),
        ("hostname", "Display the system's hostname", "hostname"),
        ("uptime", "System uptime", "uptime"),
        ("top", "Show running processes", "top"),
        ("free -h", "Show memory usage", "free -h"),
        ("df -h", "Show disk space usage", "df -h"),
    ],
    "File and Directory Management": [
        ("ls", "List directory contents", "ls -l"),
        ("cd <dir>", "Change directory", "cd /var/log"),
        ("pwd", "Print current directory", "pwd"),
        ("mkdir <dir>", "Make a new directory", "mkdir myfolder"),
        ("rm <file>", "Remove a file", "rm file.txt"),
        ("cp <src> <dest>", "Copy file or directory", "cp file.txt backup/"),
        ("mv <src> <dest>", "Move or rename file", "mv file.txt newname.txt"),
    ],
    "File Viewing and Editing": [
        ("cat <file>", "Show file contents", "cat notes.txt"),
        ("less <file>", "Scroll through file", "less bigfile.txt"),
        ("nano <file>", "Edit file in Nano", "nano notes.txt"),
        ("vim <file>", "Edit file in Vim", "vim notes.txt"),
        ("touch <file>", "Create an empty file", "touch new.txt"),
    ],
    "Search and Filter": [
        ("grep <pattern> <file>", "Search in file", "grep error log.txt"),
        ("find <path> -name <file>", "Find files", "find /home -name '*.txt'"),
        ("locate <file>", "Locate file quickly", "locate file.txt"),
        ("awk '{print $1}'", "Print first column", "awk '{print $1}' file.txt"),
    ],
    "Package Management (APT)": [
        ("sudo apt update", "Update package index", "sudo apt update"),
        ("sudo apt upgrade", "Upgrade all packages", "sudo apt upgrade"),
        ("sudo apt install <pkg>", "Install a package", "sudo apt install curl"),
        ("sudo apt remove <pkg>", "Remove a package", "sudo apt remove nano"),
    ],
    "Permissions and Ownership": [
        ("chmod +x <file>", "Make file executable", "chmod +x script.sh"),
        ("chmod 755 <file>", "Set permissions", "chmod 755 file.sh"),
        ("chown user:group <file>", "Change file owner", "chown john:admin file.txt"),
        ("ls -l", "Show file permissions", "ls -l"),
    ],
    "Networking": [
        ("ip a", "Show network interfaces", "ip a"),
        ("ping <host>", "Ping a host", "ping google.com"),
        ("curl <url>", "Fetch URL", "curl https://example.com"),
        ("wget <url>", "Download file", "wget https://file.com/file.zip"),
    ],
}

# Generate PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Linux Commands Cheat Sheet", ln=True, align="C")
pdf.ln(10)

for category, commands in linux_commands.items():
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, txt=category, ln=True)
    pdf.set_font("Arial", size=11)
    for cmd, desc, example in commands:
        pdf.multi_cell(0, 8, txt=f"  {cmd}\n    ➤ {desc}\n    ⤷ Example: {example}", border=0)
    pdf.ln(5)

pdf.output("linux_cheat_sheet.pdf")

# Generate Image (summary)
image_width, image_height = 1000, 1400
img = Image.new("RGB", (image_width, image_height), color="white")
draw = ImageDraw.Draw(img)
font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)

y_offset = 20
draw.text((20, y_offset), "Linux Commands Cheat Sheet", fill="black", font=font_title)
y_offset += 60

for category, commands in list(linux_commands.items())[:4]:
    draw.text((20, y_offset), category, fill="black", font=font_text)
    y_offset += 30
    for cmd, desc, example in commands[:3]:
        draw.text((40, y_offset), f"{cmd} - {desc}", fill="black", font=font_text)
        y_offset += 25
        draw.text((60, y_offset), f"e.g., {example}", fill="gray", font=font_text)
        y_offset += 30
    y_offset += 10

img.save("linux_cheat_sheet_image.png")
