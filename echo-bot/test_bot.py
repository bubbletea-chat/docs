"""
Simple test script for the echo bot
"""

import requests
import json
import time
import sys


def test_echo_bot():
    """Test the echo bot functionality"""
    
    base_url = "http://localhost:8000"
    
    print("🧪 Testing Echo Bot")
    print("=" * 30)
    
    # Test 1: Health check
    print("1. Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            print("   ✅ Health check passed")
            data = response.json()
            print(f"   Bot name: {data.get('bot_name')}")
            print(f"   Streaming: {data.get('streaming')}")
        else:
            print(f"   ❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("   ❌ Cannot connect to server. Make sure it's running.")
        return False
    
    # Test 2: Basic echo
    print("\n2. Testing basic echo...")
    try:
        payload = {"type": "user", "message": "Hello echo bot!"}
        response = requests.post(f"{base_url}/chat", json=payload, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            components = data.get('responses', [])
            print(f"   ✅ Received {len(components)} components")
            
            # Check component types
            types = [comp.get('type') for comp in components]
            expected_types = ['text', 'markdown', 'text']
            
            for comp in components:
                comp_type = comp.get('type')
                content = comp.get('content', comp.get('label', comp.get('url', '')))
                preview = content[:50] + "..." if len(content) > 50 else content
                print(f"   📦 {comp_type}: {preview}")
            
            if all(t in types for t in ['text', 'markdown']):
                print("   ✅ All expected component types found")
            else:
                print(f"   ⚠️  Expected components: {expected_types}")
                print(f"   Found: {types}")
                
        else:
            print(f"   ❌ Chat failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False
    
    # Test 3: Image request
    print("\n3. Testing image request...")
    try:
        payload = {"type": "user", "message": "show me an image"}
        response = requests.post(f"{base_url}/chat", json=payload, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            components = data.get('responses', [])
            
            # Check if image component is present
            has_image = any(comp.get('type') == 'image' for comp in components)
            
            if has_image:
                print("   ✅ Image component found")
                image_comp = next(comp for comp in components if comp.get('type') == 'image')
                print(f"   🖼️  Image URL: {image_comp.get('url')}")
            else:
                print("   ❌ No image component found")
                return False
                
        else:
            print(f"   ❌ Image request failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False
    
    print(f"\n{'='*30}")
    print("🎉 All tests passed!")
    print("✅ Echo bot is working correctly")
    return True


def main():
    """Main test runner"""
    
    print("🔄 Echo Bot Test Runner")
    print("Make sure the bot is running: python echo_bot.py")
    print("Waiting 2 seconds for server to be ready...")
    time.sleep(2)
    
    success = test_echo_bot()
    
    if success:
        print("\n🎯 Test completed successfully!")
        print("The BubbleTea minimal package is working correctly.")
    else:
        print("\n❌ Tests failed!")
        print("Check the server logs and try again.")
        sys.exit(1)


if __name__ == "__main__":
    main()