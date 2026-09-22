import subprocess
import sys

# pcapng files from omg1 wireshark captures.
files = [
    "01-utan-vpn-omg1.pcapng",
    "02-wireguard-omg1.pcapng",
    "03-nordvpn-omg1.pcapng",
    "04-protonvpn-omg1.pcapng",
]

def run_tshark(file, display_filter, fields):
    #Run tshark against the pcapng with a display filter and return the matching lines as a list. Return none if tshark fails instead of crashing the script
    try:
        result = subprocess.run(
            # Fields appends the -e flags at the end of the command
            ["tshark", "-r", file, "-Y", display_filter, "-T", "fields"] + fields,
            capture_output=True,
            text=True,
            check=True,
        )
    # To prevent script from crashing incase T-shark isnt found or installed.
    except FileNotFoundError:
        print("\nFAILED - tshark was not found. Make sure TShark is installed and available in PATH")
        return None
    except subprocess.CalledProcessError as e:
        print(f"\n{file}: FAILED - {e.stderr.strip()}")
        return None
    # Remove rows without extracted field values.  
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]

def analyze_dns(file):
    # Answers which domains are visible in cleartext via DNS per scenario
    rows = run_tshark(file, "dns.flags.response == 0", ["-e", "dns.qry.name"])
    if rows is None:
        return
    unique = sorted({
        name.strip()
        for row in rows
        for name in row.split(",")
        if name.strip()
    })
    print(f"\n{file}")
    print(f"{len(rows)} Packets containing DNS queries")
    print(f"{len(unique)} Unique queried names")
    for d in unique:
        print(f" {d}")

def analyze_http(file):
    # FInd HTTP requests, excluding SSDP discovery traffic.
    rows = run_tshark(file, "http.request and not ssdp", ["-e", "http.host", "-e", "http.request.uri"])
    if rows is None:
        return

    print(f"\n{file}")
    print(f"{len(rows)} Packets containing HTTP requests (excluding SSDP)")
    for r in rows:
        print(f" {r}")

def analyze_sni(file):
    # Answers which server names are visible via TLS SNI.
    rows = run_tshark(file, "tls.handshake.type == 1", ["-e", "tls.handshake.extensions_server_name"])
    if rows is None:
        return
    unique = sorted(set(rows))
    print(f"\n{file}")
    print(f"{len(rows)} Packets containing visible TLS SNI")
    print(f"{len(unique)} Unique server names:")
    for n in unique:
        print(f" {n}")

# Maps a command argument to the function I want to run.
functions = {
    "dns": analyze_dns,
    "http": analyze_http,
    "sni": analyze_sni,
}

if __name__ == "__main__":
    # Validate the argument before running anything, so a typo gives a message instead of instantly crashing
    valid_choices = list(functions.keys()) + ["all"]

    if len(sys.argv) != 2 or sys.argv[1] not in valid_choices:
        print("Usage: python trafikanalys.py [dns|http|sni|all]")
        sys.exit(1)

    choice = sys.argv[1]

    if choice == "all":
        for file in files:
            analyze_dns(file)
            analyze_http(file)
            analyze_sni(file)
    else:
        for file in files:
            functions[choice](file)    
