# IBM Cloud Deployment Guide for CodeCompass

This guide will help you deploy the CodeCompass application to IBM Cloud using Cloud Foundry.

## Prerequisites

1. **IBM Cloud Account**: Sign up at [cloud.ibm.com](https://cloud.ibm.com)
2. **IBM Cloud CLI**: Install from [IBM Cloud CLI Documentation](https://cloud.ibm.com/docs/cli)
3. **Cloud Foundry CLI**: Included with IBM Cloud CLI
4. **Required API Keys**:
   - IBM watsonx.ai API Key
   - IBM watsonx.ai Project ID
   - GitHub Personal Access Token (optional, for private repos)

## Step 1: Install IBM Cloud CLI

### Windows
```powershell
# Download and run the installer from:
# https://cloud.ibm.com/docs/cli?topic=cli-install-ibmcloud-cli
```

### macOS
```bash
curl -fsSL https://clis.cloud.ibm.com/install/osx | sh
```

### Linux
```bash
curl -fsSL https://clis.cloud.ibm.com/install/linux | sh
```

## Step 2: Login to IBM Cloud

```bash
# Login to IBM Cloud
ibmcloud login

# If using SSO
ibmcloud login --sso

# Target Cloud Foundry
ibmcloud target --cf
```

## Step 3: Set Environment Variables

Before deploying, you need to set your environment variables in IBM Cloud:

```bash
# Set watsonx.ai API Key
ibmcloud cf set-env codecompass WATSONX_API_KEY "your-watsonx-api-key"

# Set watsonx.ai Project ID
ibmcloud cf set-env codecompass WATSONX_PROJECT_ID "your-project-id"

# Set GitHub Token (optional)
ibmcloud cf set-env codecompass GITHUB_TOKEN "your-github-token"
```

**Alternative**: You can also set these in the IBM Cloud dashboard:
1. Go to your app in IBM Cloud Console
2. Navigate to "Runtime" → "Environment Variables"
3. Add the variables there

## Step 4: Deploy the Application

### Option A: Deploy from Local Directory

```bash
# Navigate to your project directory
cd e:/codecompass

# Deploy to IBM Cloud
ibmcloud cf push codecompass
```

### Option B: Deploy with Custom Settings

```bash
# Deploy with specific memory and instances
ibmcloud cf push codecompass -m 512M -i 1
```

### Option C: Deploy with Custom Route

```bash
# Deploy with a custom route
ibmcloud cf push codecompass --hostname your-custom-name
```

## Step 5: Verify Deployment

```bash
# Check app status
ibmcloud cf app codecompass

# View logs
ibmcloud cf logs codecompass --recent

# Stream live logs
ibmcloud cf logs codecompass
```

## Step 6: Access Your Application

After successful deployment, your app will be available at:
- Default: `https://codecompass.mybluemix.net`
- Custom: `https://your-custom-name.mybluemix.net`

Test the health endpoint:
```bash
curl https://codecompass.mybluemix.net/health
```

## Configuration Files

The deployment uses these configuration files:

### manifest.yml
Defines the application configuration:
- Memory: 512MB
- Instances: 1
- Buildpack: Python
- Health check endpoint: /health

### Procfile
Specifies the command to start the application:
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

### runtime.txt
Specifies Python version:
```
python-3.11.x
```

### .cfignore
Lists files to exclude from deployment (similar to .gitignore)

## Environment Variables Required

| Variable | Description | Required |
|----------|-------------|----------|
| `WATSONX_API_KEY` | IBM watsonx.ai API Key | Yes |
| `WATSONX_PROJECT_ID` | IBM watsonx.ai Project ID | Yes |
| `GITHUB_TOKEN` | GitHub Personal Access Token | No |

## Troubleshooting

### App Won't Start
```bash
# Check logs for errors
ibmcloud cf logs codecompass --recent

# Restart the app
ibmcloud cf restart codecompass
```

### Memory Issues
```bash
# Increase memory allocation
ibmcloud cf scale codecompass -m 1G
```

### Environment Variables Not Set
```bash
# List all environment variables
ibmcloud cf env codecompass

# Set missing variables
ibmcloud cf set-env codecompass VARIABLE_NAME "value"

# Restage after setting variables
ibmcloud cf restage codecompass
```

### Port Binding Issues
The app automatically uses the `$PORT` environment variable provided by Cloud Foundry. No manual configuration needed.

## Scaling Your Application

### Horizontal Scaling (More Instances)
```bash
# Scale to 3 instances
ibmcloud cf scale codecompass -i 3
```

### Vertical Scaling (More Memory)
```bash
# Scale to 1GB memory
ibmcloud cf scale codecompass -m 1G
```

## Updating Your Application

```bash
# Make your code changes locally
# Then push the update
ibmcloud cf push codecompass

# Or use zero-downtime deployment
ibmcloud cf push codecompass --strategy rolling
```

## Monitoring

### View App Information
```bash
ibmcloud cf app codecompass
```

### View Recent Logs
```bash
ibmcloud cf logs codecompass --recent
```

### Stream Live Logs
```bash
ibmcloud cf logs codecompass
```

### View Events
```bash
ibmcloud cf events codecompass
```

## Cost Optimization

- **Lite Plan**: Free tier available with limitations
- **Standard Plan**: Pay-as-you-go based on memory and instances
- **Optimize**: Use 512MB memory for development, scale up for production

## Security Best Practices

1. **Never commit .env files** - Already in .gitignore
2. **Use IBM Cloud environment variables** for secrets
3. **Rotate API keys regularly**
4. **Enable HTTPS** (automatic with IBM Cloud)
5. **Monitor access logs** regularly

## Additional Resources

- [IBM Cloud Documentation](https://cloud.ibm.com/docs)
- [Cloud Foundry Documentation](https://docs.cloudfoundry.org/)
- [IBM watsonx.ai Documentation](https://www.ibm.com/docs/en/watsonx-as-a-service)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## Quick Reference Commands

```bash
# Login
ibmcloud login

# Target Cloud Foundry
ibmcloud target --cf

# Deploy
ibmcloud cf push codecompass

# View logs
ibmcloud cf logs codecompass --recent

# Restart
ibmcloud cf restart codecompass

# Scale
ibmcloud cf scale codecompass -i 2 -m 1G

# Delete app
ibmcloud cf delete codecompass
```

## Support

For issues or questions:
- IBM Cloud Support: [cloud.ibm.com/unifiedsupport](https://cloud.ibm.com/unifiedsupport)
- watsonx.ai Community: [community.ibm.com](https://community.ibm.com)

---

**Generated by IBM watsonx.ai (Bob) — IBM Bob Dev Day Hackathon**
**Model: ibm/granite-3-8b-instruct | Platform: IBM Cloud**