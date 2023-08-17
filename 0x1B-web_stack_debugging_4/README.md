<h1>0x1B-web_stack_debugging_4</h1>

<p>In this project i will be debugging a server to fix its issues.</p>
<p> After running <i>ab -c 100 -n 2000 localhost/"</i>, i received a number of failed request which should not be so. Next i ran <i>tail -n 3 /var/log/nginx/error.log</i> to identify what is causing the failed request. I received <i>accept4() failed (24: Too many open files)</i> among the erros which indicated that the number of requests had surpassed the nginx file limit. Based on the error, I checked <i>/etc/default/nginx</i> and increased the limit to 12000. I ran <i>ab -c 100 -n 2000 localhost/</i> and received 0 failed requests. The puppet file above just automated the whole process</p>

<h6>Using:</h6>
<p>Ubuntu 14.04</p>
<p>puppet-lint version 2.1.1</p>
