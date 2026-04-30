DataTransfer(cartOpen,false)

total();{
  return this.cart.reduce((a,b)=>a+b.price,0)
}

checkout();{
  this.toast = "Redirigiendo a pago 💳 (simulado)"
  setTimeout(()=>{
    this.toast="Pago completado ✅"
    this.cart=[]
  },2000)
}

sendForm();{
  if(!this.form.name || !this.form.email || !this.form.msg){
    this.toast="Completa todos los campos"
  } else if(!this.form.email.includes("@")){
    this.toast="Email inválido"
  } else {
    this.toast="Mensaje enviado 🚀"
    this.form={name:"",email:"",msg:""}
  }
  setTimeout(()=>this.toast="",2000)
}