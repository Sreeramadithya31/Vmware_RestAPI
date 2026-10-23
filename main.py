from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import os

app = FastAPI(
    title="VMware Workstation REST API",
    description="REST API for controlling VMware Workstation virtual machines",
    version="1.0.0"
)

VMRUN = r"D:\vmrun.exe"


class VMRequest(BaseModel):
    vmx_path: str


def run_vmrun(command: list[str]):
    """Run vmrun and return its output."""
    if not os.path.exists(VMRUN):
        raise HTTPException(
            status_code=500,
            detail=f"vmrun.exe not found at {VMRUN}"
        )

    try:
        result = subprocess.run(
            [VMRUN, "-T", "ws"] + command,
            capture_output=True,
            text=True,
            timeout=30
        )

        return {
            "success": result.returncode == 0,
            "output": result.stdout.strip(),
            "error": result.stderr.strip(),
            "return_code": result.returncode
        }

    except subprocess.TimeoutExpired:
        raise HTTPException(
            status_code=500,
            detail="VMware command timed out"
        )


@app.get("/")
def root():
    return {
        "project": "VMware Workstation REST API",
        "status": "running"
    }


@app.get("/vms")
def list_vms():
    """List currently running virtual machines."""
    return run_vmrun(["list"])


@app.get("/vm/status")
def vm_status():
    """Check whether VMware is accessible."""
    if not os.path.exists(VMRUN):
        raise HTTPException(
            status_code=500,
            detail="vmrun.exe not found"
        )

    result = subprocess.run(
        [VMRUN, "-T", "ws", "list"],
        capture_output=True,
        text=True
    )

    output = result.stdout.strip()

    return {
        "success": result.returncode == 0,
        "status": "VMware accessible",
        "running_vms": output
    }


@app.post("/vm/start")
def start_vm(request: VMRequest):
    """Start a virtual machine."""
    if not os.path.exists(request.vmx_path):
        raise HTTPException(
            status_code=404,
            detail=f"VMX file not found: {request.vmx_path}"
        )

    return run_vmrun([
        "start",
        request.vmx_path,
        "gui"
    ])


@app.post("/vm/stop")
def stop_vm(request: VMRequest):
    """Stop a virtual machine."""
    if not os.path.exists(request.vmx_path):
        raise HTTPException(
            status_code=404,
            detail=f"VMX file not found: {request.vmx_path}"
        )

    return run_vmrun([
        "stop",
        request.vmx_path,
        "soft"
    ])


@app.post("/vm/suspend")
def suspend_vm(request: VMRequest):
    """Suspend a virtual machine."""
    if not os.path.exists(request.vmx_path):
        raise HTTPException(
            status_code=404,
            detail=f"VMX file not found: {request.vmx_path}"
        )

    return run_vmrun([
        "suspend",
        request.vmx_path,
        "soft"
    ])


@app.post("/vm/reset")
def reset_vm(request: VMRequest):
    """Reset a virtual machine."""
    if not os.path.exists(request.vmx_path):
        raise HTTPException(
            status_code=404,
            detail=f"VMX file not found: {request.vmx_path}"
        )

    return run_vmrun([
        "reset",
        request.vmx_path,
        "soft"
    ])


@app.get("/host/networks")
def host_networks():
    """List VMware host networks."""
    return run_vmrun(["listHostNetworks"])