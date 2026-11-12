# Experiment 9 — Healthcare DevSecOps

A synthetic-data healthcare dashboard deployed to K3s by Jenkins. All Kubernetes resources are isolated in namespace `healthcare`; Experiment 8's `bluegreen` namespace, files, NodePort 30081 and BlueGreen-Pipeline remain untouched.

## Jenkins
Create **DevSecOps-Pipeline** → Pipeline script from SCM → Git `https://github.com/Parth4950/deploy-flow.git` → branch `*/main` → Script Path `experiment-9/Jenkinsfile`.

The Jenkins agent requires Docker, kubectl, K3s kubeconfig at `/var/lib/jenkins/.kube/config`, and the same restricted sudo permission for K3s containerd image imports used by Experiment 8. Scanner tools run as Docker containers.

## Pipeline
Gitleaks (secrets) → Semgrep (SAST) → Checkov (Kubernetes IaC, soft-fail reporting) → Trivy (filesystem/dependencies) → Syft (CycloneDX SBOM) → Grype (HIGH+ SBOM gate) → Docker build → Trivy image scan → K3s deploy → rollout verification.

Blocking scans stop deployment. Frontend NodePort: **30082**. Add inbound TCP 30082 to the EC2 security group; keep Experiment 8 TCP 30081. Open `http://EC2_PUBLIC_IP:30082` after successful deployment. All patient profiles and medical records are synthetic demo data.
