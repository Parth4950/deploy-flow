# Experiment 8 — Automated Blue-Green Deployment

All Kubernetes resources are isolated in namespace `bluegreen`. Experiment 7 files at the repository root are unchanged.

Create a Jenkins Pipeline job named `BlueGreen-Pipeline`:
- Definition: Pipeline script from SCM
- SCM: Git
- Repository: https://github.com/Parth4950/deploy-flow.git
- Branch: */main
- Script Path: experiment-8/Jenkinsfile

The Jenkins agent uses existing Docker access, K3s kubeconfig and the restricted sudo permission for importing images into K3s containerd.

The pipeline deploys two replicas to the inactive color, waits for rollout and readiness checks, then switches the `bg-production` Service selector. If checks fail, production traffic stays on the previous color.

NodePort: 30081. Add inbound TCP 30081 to the EC2 security group after the first successful deployment, then browse to http://EC2_PUBLIC_IP:30081.
