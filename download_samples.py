#!/usr/bin/env python3
"""
LlamaStyles Sample Downloader

This script downloads sample content and style images
for use with the LlamaStyles application.
"""

import os
import requests
import zipfile
import io
import shutil
from pathlib import Path
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, DownloadColumn, TransferSpeedColumn

# Set up Rich console for pretty output
console = Console()

# Sample image sets to download
SAMPLE_SETS = {
    "basic": {
        "url": "https://github.com/yourusername/llamastyles-samples/raw/main/basic_samples.zip",
        "description": "Basic content and style samples (10 images, 5MB)"
    },
    "artistic": {
        "url": "https://github.com/yourusername/llamastyles-samples/raw/main/artistic_samples.zip",
        "description": "Artistic style samples including paintings and illustrations (20 images, 15MB)"
    },
    "photos": {
        "url": "https://github.com/yourusername/llamastyles-samples/raw/main/photo_samples.zip",
        "description": "High-quality photographic content samples (15 images, 25MB)"
    }
}

def download_file(url):
    """Download a file and return its content"""
    with Progress(
        TextColumn("[bold blue]{task.description}", justify="right"),
        BarColumn(bar_width=40),
        DownloadColumn(),
        TransferSpeedColumn()
    ) as progress:
        task = progress.add_task(f"Downloading...", total=None)
        
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Get content length if available
        total_size = int(response.headers.get('content-length', 0))
        if total_size:
            progress.update(task, total=total_size)
            
        chunks = []
        downloaded = 0
        for chunk in response.iter_content(chunk_size=1024*1024):
            chunks.append(chunk)
            downloaded += len(chunk)
            if total_size:
                progress.update(task, completed=downloaded)
        
        progress.update(task, completed=downloaded)
        return b''.join(chunks)

def main():
    """Main function to download and extract samples"""
    # Create samples directory if it doesn't exist
    samples_dir = Path("samples")
    if not samples_dir.exists():
        samples_dir.mkdir(parents=True)
    
    console.print("[bold]LlamaStyles Sample Downloader[/bold]")
    console.print("This tool will download sample images for use with LlamaStyles.\n")
    
    # Display available sample sets
    console.print("[bold]Available sample sets:[/bold]")
    for key, info in SAMPLE_SETS.items():
        console.print(f"[green]{key}[/green]: {info['description']}")
    
    # Ask which set to download
    choice = console.input("\n[bold]Enter sample set to download (basic, artistic, photos, all) or 'q' to quit:[/bold] ")
    
    if choice.lower() == 'q':
        console.print("[yellow]Exiting...[/yellow]")
        return
    
    # Determine which sets to download
    sets_to_download = []
    if choice.lower() == 'all':
        sets_to_download = list(SAMPLE_SETS.keys())
    elif choice.lower() in SAMPLE_SETS:
        sets_to_download = [choice.lower()]
    else:
        console.print("[bold red]Invalid choice. Please run the script again.[/bold red]")
        return
    
    # Download and extract each selected set
    for set_name in sets_to_download:
        set_info = SAMPLE_SETS[set_name]
        console.print(f"\n[bold]Downloading {set_name} sample set...[/bold]")
        
        try:
            # Download the zip file
            zip_content = download_file(set_info['url'])
            
            # Extract the zip file
            with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_ref:
                console.print(f"[bold]Extracting {len(zip_ref.namelist())} files to samples/{set_name}/...[/bold]")
                
                # Create set directory
                set_dir = samples_dir / set_name
                if set_dir.exists():
                    console.print(f"[yellow]Directory samples/{set_name} already exists. Removing...[/yellow]")
                    shutil.rmtree(set_dir)
                
                set_dir.mkdir(parents=True)
                
                # Extract files
                zip_ref.extractall(set_dir)
            
            console.print(f"[bold green]✓[/bold green] {set_name} samples downloaded and extracted successfully!")
            
        except Exception as e:
            console.print(f"[bold red]Error downloading {set_name} samples:[/bold red] {str(e)}")
    
    console.print("\n[bold green]All downloads complete![/bold green]")
    console.print("[bold]To use these samples with LlamaStyles, run:[/bold]")
    console.print("[cyan]  python run_llamastyles.py interactive[/cyan]")
    console.print("and select from the downloaded samples when prompted.")

if __name__ == "__main__":
    main() 