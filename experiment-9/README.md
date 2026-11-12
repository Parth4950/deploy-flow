# Experiment 9 — Healthcare DevSecOps

A synthetic-data healthcare dashboard deployed to K3s by Jenkins. All Kubernetes resources are isolated in namespace `healthcare`; Experiment 8's `bluegreen` namespace, files, NodePort 30081 and BlueGreen-Pipeline remain untouched.

## Application

The CareFlow dashboard includes:
- Facility overview with patient-visit chart, department load, appointment summary and care team
- Patient directory, appointment schedule, doctor directory and medical-record views
- Search across patients, appointments, doctors and medical records
- Responsive desktop/mobile layout and a clearly labelled demo appointment form
- FastAPI endpoints backed only by synthetic sample data

The appointment form is intentionally frontend-only: it does not create a real appointment or transmit patient information. This is a classroom demonstration, not a clinical system.

## Run locally

Backend:
```bash
cd experiment-9/backend
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Frontend (in a second terminal):
```bash
cd experiment-9/frontend
npm install
npm run dev
```

Vite proxies `/api` requests to `http://localhost:8000`.

## Jenkins

Create **DevSecOps-Pipeline** → Pipeline script from SCM → Git `https://github.com/Parth4950/deploy-flow.git` → branch `*/main` → Script Path `experiment-9/Jenkinsfile`.

The Jenkins agent requires Docker, kubectl, K3s kubeconfig at `/var/lib/jenkins/.kube/config`, and the same restricted sudo permission for K3s containerd image imports used by Experiment 8. Scanner tools run as Docker containers.

## Pipeline

Gitleaks (secrets) → Semgrep (SAST) → Checkov (Kubernetes IaC, soft-fail reporting) → Trivy (filesystem/dependencies) → Syft (CycloneDX SBOM) → Grype (HIGH+ SBOM gate) → Docker build → Trivy image scan → K3s deploy → rollout verification.

Blocking scans stop deployment. Frontend NodePort: **30082**. Add inbound TCP 30082 to the EC2 security group; keep Experiment 8 TCP 30081. Open `http://EC2_PUBLIC_IP:30082` after successful deployment. All patient profiles and medical records are synthetic demo data.

## Isolation guarantee

Experiment 9 deploys only into namespace `healthcare` and uses NodePort `30082`. Do not delete or replace Experiment 8 resources: its `bluegreen` namespace and NodePort `30081` are intentionally retained and can run alongside this experiment.
