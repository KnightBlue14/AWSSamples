Terraform is a tool from Hashicorp that allows you to create templates for provisioning resources that can be quickly spun up when needed, and can be used in a wide variety of cases, including AWS. This folder provides an example, as well as breaking down the beginning steps to use it.

First, you will need to download the tool from the Hashicorp website, found here 
```
https://developer.hashicorp.com/terraform/install
```
On Linux, you will need to use the method for your package manager, including Amazon Linux.

That done, we can set up our environment, using 
```
terraform init
```
It will generate files not found in this repo - you don't need to edit them, they just allow terraform to work.

Next, we create our template, such as text.tf, specifying the type of resource and it's name, in this case 'local_file' and 'pets'. The name can be whatever suits your needs.

For the content, we give the full filename, and the content of the file, here a simple text string.

Now that the file is setup, we can go over the next few commands.
```
terraform validate 
```
-- checks your file to make sure it is syntactically correct (though do be aware that it may still not work if it is not properly set up, i.e. mislabeled variables)

```
terraform plan
```
 -- previews what changes will be made, allowing you to double check for any mistakes (again, the files themselves working is a separate matter)

```
terraform apply
```
 -- commits the changes. In this case, it will create a file called pets.txt, with the content "I have a dog called Spot". This is a very simple use case, but even this on its own has potential uses, such as scripts or or creating multiple files from one template. Furthermore, terraform will continue to track them after creation, which is where the final command comes in

```
terraform destroy
```
 -- deletes the files created earlier. If there are issues with files, or changes that need to be made, this will allow you to remove all of them, make the necessary changes, and then restore them, rather than needing to edit multiple files.